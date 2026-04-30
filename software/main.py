# main.py — NFC Drawer Lock
# ESP32-C3 + PN532 (I2C) + Servo (rack & pinion)

from machine import Pin, PWM, I2C
import time
from pn532 import PN532, PN532Error

# ── Pin assignments ────────────────────────────────────────────
SERVO_PIN = 13   # Servo signal
SDA_PIN   = 21   # PN532 SDA
SCL_PIN   = 22   # PN532 SCL

# ── Servo angles (rack & pinion) ──────────────────────────────
# Clockwise → rack extends → bolt locks → higher angle = locked
#
# ┌─ CALIBRATION ───────────────────────────────────────────────┐
# │ If rack doesn't fully extend when locking:                 │
# │   → increase LOCKED_DEG in 10° steps (max ~170°)           │
# │ If rack doesn't fully retract when unlocking:              │
# │   → decrease UNLOCKED_DEG in 10° steps (min ~10°)          │
# │ Leave ~5° margin at each end — stalling kills the motor.   │
# └─────────────────────────────────────────────────────────────┘
LOCKED_DEG   = 90
UNLOCKED_DEG = 0

# ── Timing ────────────────────────────────────────────────────
DEBOUNCE_MS = 800
SCAN_MS     = 100


# ═════════════════════════════════════════════════════════════
# SERVO
# ═════════════════════════════════════════════════════════════

servo = PWM(Pin(SERVO_PIN), freq=50)

def _angle_to_duty(deg):
    return int(26 + (deg / 180.0) * (128 - 26))

def move_servo(deg):
    servo.duty(_angle_to_duty(deg))


# ═════════════════════════════════════════════════════════════
# LOCK STATE
# ═════════════════════════════════════════════════════════════

locked = True
move_servo(LOCKED_DEG)
print("[BOOT] Drawer LOCKED. Waiting for NFC card...")

def toggle_lock():
    global locked
    if locked:
        move_servo(UNLOCKED_DEG)
        locked = False
        print("[NFC]  Card detected → UNLOCKED")
    else:
        move_servo(LOCKED_DEG)
        locked = True
        print("[NFC]  Card detected → LOCKED")


# ═════════════════════════════════════════════════════════════
# NFC SETUP
# ═════════════════════════════════════════════════════════════

i2c = I2C(0, sda=Pin(SDA_PIN), scl=Pin(SCL_PIN), freq=100_000)

devices = i2c.scan()
print("[I2C]  Devices found:", ["0x{:02X}".format(d) for d in devices])
if 0x24 not in devices:
    print("[ERR]  PN532 not found at 0x24. Check wiring.")
    raise SystemExit

nfc = PN532(i2c)
try:
    nfc.SAM_configuration()
    print("[NFC]  PN532 ready. Scan any card to lock/unlock.")
except PN532Error as e:
    print("[ERR]  SAM config failed:", e)
    raise SystemExit


# ═════════════════════════════════════════════════════════════
# MAIN LOOP
# ═════════════════════════════════════════════════════════════

last_trigger = time.ticks_ms()

while True:
    try:
        uid = nfc.read_passive_target(timeout_ms=300)
    except PN532Error as e:
        print("[ERR]  Read error:", e)
        time.sleep_ms(500)
        continue

    now = time.ticks_ms()

    if uid and time.ticks_diff(now, last_trigger) > DEBOUNCE_MS:
        print("[NFC]  UID:", " ".join("{:02X}".format(b) for b in uid))
        toggle_lock()
        last_trigger = now

    time.sleep_ms(SCAN_MS)
