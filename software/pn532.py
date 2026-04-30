# pn532.py — MicroPython PN532 NFC driver (I2C)
# Used by main.py when SIM_MODE = False (real hardware only)
# ──────────────────────────────────────────────────────────────

from machine import I2C
import time

# ── Constants ─────────────────────────────────────────────────
_ADDR       = 0x24        # Default PN532 I2C address
_PREAMBLE   = 0x00
_STARTCODE  = b'\x00\xFF'
_POSTAMBLE  = 0x00
_TFI_OUT    = 0xD4        # Frame direction: Host → PN532
_TFI_IN     = 0xD5        # Frame direction: PN532 → Host
_ACK_FRAME  = b'\x00\x00\xFF\x00\xFF\x00'  # Expected ACK bytes (after status byte)

CMD_SAMCONFIG     = 0x14  # Configure SAM (Security Access Module)
CMD_INLISTPASSIVE = 0x4A  # Detect passive (ISO14443A) targets
BAUD_ISO14443A    = 0x00  # 106 kbps — covers Mifare, NTAG, most NFC cards


# ── Helpers ───────────────────────────────────────────────────

def _lcs(length):
    """Length checksum: (~LEN + 1) & 0xFF  →  LEN + LCS == 0x00 mod 256."""
    return (~length + 1) & 0xFF

def _dcs(data):
    """Data checksum: (~sum(data) + 1) & 0xFF  →  sum(data) + DCS == 0x00 mod 256."""
    return (~sum(data) + 1) & 0xFF

def _build_frame(cmd, params=()):
    """
    Assemble a PN532 normal information frame.
    Layout: PREAMBLE | 0x00 0xFF | LEN | LCS | TFI | CMD | PARAMS | DCS | POSTAMBLE
    """
    body   = bytes([_TFI_OUT, cmd]) + bytes(params)
    length = len(body)
    return (bytes([_PREAMBLE]) + _STARTCODE
            + bytes([length, _lcs(length)])
            + body
            + bytes([_dcs(body), _POSTAMBLE]))


# ── Driver ────────────────────────────────────────────────────

class PN532Error(Exception):
    pass


class PN532:
    def __init__(self, i2c, addr=_ADDR):
        self._i2c  = i2c
        self._addr = addr

    # ── Low-level ──────────────────────────────────────────────

    def _wait_ready(self, timeout_ms=1000):
        """Poll the PN532 status byte until the RDY bit (bit 0) is set."""
        deadline = time.ticks_add(time.ticks_ms(), timeout_ms)
        while time.ticks_diff(deadline, time.ticks_ms()) > 0:
            try:
                if self._i2c.readfrom(self._addr, 1)[0] & 0x01:
                    return True
            except OSError:
                pass
            time.sleep_ms(10)
        return False

    def _send_cmd(self, cmd, params=()):
        """
        Write a command frame and verify the ACK.
        PN532 responds to every command with a 6-byte ACK before the actual response.
        """
        self._i2c.writeto(self._addr, _build_frame(cmd, params))
        time.sleep_ms(5)

        if not self._wait_ready(500):
            raise PN532Error("Timeout waiting for ACK after cmd 0x{:02X}".format(cmd))

        # ACK frame is 7 bytes: status byte + 0x00 0x00 0xFF 0x00 0xFF 0x00
        ack = self._i2c.readfrom(self._addr, 7)
        if ack[1:7] != _ACK_FRAME:
            raise PN532Error("Bad ACK: {}".format(list(ack)))

    def _read_response(self, payload_len, timeout_ms=1000):
        """
        Read a response frame after a command.
        Returns `payload_len` bytes of the DATA portion, or None on timeout.

        Frame layout received:
          [status] [0x00] [0x00 0xFF] [LEN] [LCS] [0xD5] [CMD+1] [DATA...] [DCS] [0x00]
           idx 0    1       2   3       4     5      6       7      8+
        """
        if not self._wait_ready(timeout_ms):
            return None
        # Total bytes to read: 1(status) + 2(preamble+start) + 2(start) + 2(len+lcs)
        #                     + 2(TFI+CMD+1) + payload_len + 1(dcs) + 1(post) = payload_len + 9
        buf = self._i2c.readfrom(self._addr, payload_len + 9)
        return bytes(buf[8 : 8 + payload_len])

    # ── Public API ─────────────────────────────────────────────

    def SAM_configuration(self):
        """
        Put the PN532 into normal operating mode.
        Must be called once after power-on before scanning for cards.
        Params: mode=0x01 (normal), timeout=0x14, use_IRQ=0x01
        """
        self._send_cmd(CMD_SAMCONFIG, (0x01, 0x14, 0x01))
        self._read_response(0, timeout_ms=500)  # SAMConfig response has no data payload

    def read_passive_target(self, timeout_ms=500):
        """
        Scan for one ISO14443A NFC card/tag.

        Returns:
            bytes  — UID of the detected card (4 or 7 bytes for Mifare/NTAG)
            None   — no card found within timeout_ms

        Response layout (InListPassiveTarget, 0x4B):
          numTargets | Tg | ATQA(2) | SAK | NfcIdLen | NfcId...
            [8]       [9]  [10,11]  [12]    [13]       [14+]
        (indexes into the raw 20-byte read buffer, after status/preamble/etc.)
        """
        self._send_cmd(CMD_INLISTPASSIVE, (0x01, BAUD_ISO14443A))

        # Wait longer here: card detection itself takes time
        deadline = time.ticks_add(time.ticks_ms(), timeout_ms)
        while time.ticks_diff(deadline, time.ticks_ms()) > 0:
            try:
                if self._i2c.readfrom(self._addr, 1)[0] & 0x01:
                    break
            except OSError:
                pass
            time.sleep_ms(20)
        else:
            return None  # Timed out — no card present

        buf = self._i2c.readfrom(self._addr, 20)

        # Sanity checks
        if len(buf) < 15:
            return None
        if buf[8] == 0:          # numTargets == 0
            return None

        uid_len = buf[13]
        if len(buf) < 14 + uid_len:
            return None

        return bytes(buf[14 : 14 + uid_len])
