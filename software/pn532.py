# pn532.py — MicroPython PN532 NFC driver (I2C)
# ESP32-C3-DevKitM-1 — GPIO6 SDA, GPIO7 SCL

from machine import I2C
import time

# Constants
_ADDR = 0x24                     # Default PN532 I2C address
_PREAMBLE = 0x00
_STARTCODE = b'\x00\xFF'
_POSTAMBLE = 0x00
_TFI_OUT = 0xD4                  # Host -> PN532
_TFI_IN = 0xD5                   # PN532 -> Host
_ACK_FRAME = b'\x00\x00\xFF\x00\xFF\x00'

CMD_SAMCONFIG = 0x14             # Configure SAM
CMD_INLISTPASSIVE = 0x4A         # Detect passive targets
BAUD_ISO14443A = 0x00            # 106 kbps, works for Mifare/NTAG/most NFC tags


def _lcs(length):
    return (~length + 1) & 0xFF


def _dcs(data):
    return (~sum(data) + 1) & 0xFF


def _build_frame(cmd, params=()):
    body = bytes([_TFI_OUT, cmd]) + bytes(params)
    length = len(body)
    return (
        bytes([_PREAMBLE]) +
        _STARTCODE +
        bytes([length, _lcs(length)]) +
        body +
        bytes([_dcs(body), _POSTAMBLE])
    )


class PN532Error(Exception):
    pass


class PN532:
    def __init__(self, i2c, addr=_ADDR):
        self._i2c = i2c
        self._addr = addr

    def _wait_ready(self, timeout_ms=1000):
        """Wait until the PN532 sets the ready bit."""
        deadline = time.ticks_add(time.ticks_ms(), timeout_ms)

        while time.ticks_diff(deadline, time.ticks_ms()) > 0:
            try:
                status = self._i2c.readfrom(self._addr, 1)[0]
                if status & 0x01:
                    return True
            except OSError:
                pass

            time.sleep_ms(10)

        return False

    def _send_cmd(self, cmd, params=()):
        """Send a command frame and check for ACK."""
        frame = _build_frame(cmd, params)
        self._i2c.writeto(self._addr, frame)
        time.sleep_ms(5)

        if not self._wait_ready(500):
            raise PN532Error("Timeout waiting for ACK after cmd 0x{:02X}".format(cmd))

        ack = self._i2c.readfrom(self._addr, 7)
        if ack[1:7] != _ACK_FRAME:
            raise PN532Error("Bad ACK: {}".format(list(ack)))

    def _read_response(self, payload_len, timeout_ms=1000):
        """Read a response frame and return just the payload."""
        if not self._wait_ready(timeout_ms):
            return None

        buf = self._i2c.readfrom(self._addr, payload_len + 9)
        return bytes(buf[8:8 + payload_len])

    def SAM_configuration(self):
        """
        Put the PN532 into normal mode.
        Call this once after power-on before scanning.
        """
        self._send_cmd(CMD_SAMCONFIG, (0x01, 0x14, 0x01))
        self._read_response(0, timeout_ms=500)

    def read_passive_target(self, timeout_ms=500):
        """
        Scan for one ISO14443A card or tag.
        Returns the UID as bytes, or None if nothing is found.
        Works with Mifare Classic, NTAG, and most 13.56 MHz cards.
        """
        self._send_cmd(CMD_INLISTPASSIVE, (0x01, BAUD_ISO14443A))

        deadline = time.ticks_add(time.ticks_ms(), timeout_ms)
        while time.ticks_diff(deadline, time.ticks_ms()) > 0:
            try:
                status = self._i2c.readfrom(self._addr, 1)[0]
                if status & 0x01:
                    break
            except OSError:
                pass

            time.sleep_ms(20)
        else:
            return None

        buf = self._i2c.readfrom(self._addr, 20)

        if len(buf) < 15:
            return None

        if buf[8] == 0:
            return None

        uid_len = buf[13]
        if len(buf) < 14 + uid_len:
            return None

        return bytes(buf[14:14 + uid_len])
