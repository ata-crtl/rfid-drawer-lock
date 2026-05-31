# main.py — NFC drawer lock
# ESP32-C3-DevKitM-1 + PN532 (I2C) + SG90 servo
# Any NFC card or tag toggles the lock

from machine import Pin, PWM, I2C
import time
from pn532 import PN532, PN532Error

# Pin assignments
SERVO_PIN = 4   # Servo signal -> GPIO4
SDA_PIN = 6     # PN532 SDA -> GPIO6
SCL_PIN = 7     # PN532 SCL -> GPIO7
LED_RED = 5     # Red LED -> GPIO5

# LED setup
red_led = Pin(LED_RED, Pin.OUT)
red_led.value(1)  # Start locked

# Servo positions
# Adjust these if the servo doesn't travel far enough.
# If locking doesn't fully extend, increase LOCKED_DEG.
# If unlocking doesn't fully retract, decrease UNLOCKED_DEG.
# Leave a bit of margin at both ends so the servo doesn't stall.
LOCKED_DEG = 90
UNLOCKED_DEG = 0

# Timing
DEBOUNCE_MS = 800   # Stops one card from triggering twice
SCAN_MS = 100       # Delay between scans

servo = PWM(Pin(SERVO_PIN), freq=50)


def _angle_to_duty(deg):
    return int(26 + (deg / 180.0) * (128 - 26))


def move_servo(deg):
    servo.duty(_angle_to_duty(deg))


locked = True
move_servo(LOCKED_DEG)
red_led.value(1)

print("[BOOT] Drawer LOCKED. Scan any card to unlock.")


def toggle_lock():
    global locked

    if locked:
        move_servo(UNLOCKED_DEG)
        red_led.value(0)
        locked = False
        print("[NFC] Card detected -> UNLOCKED")
    else:
        move_servo(LOCKED_DEG)
        red_led.value(1)
        locked = True
        print("[NFC] Card detected -> LOCKED")


# NFC setup
i2c = I2C(0, sda=Pin(SDA_PIN), scl=Pin(SCL_PIN), freq=100_000)

devices = i2c.scan()
print("[I2C] Devices found:", ["0x{:02X}".format(d) for d in devices])

if 0x24 not in devices:
    print("[ERR] PN532 not found at 0x24. Check wiring and I2C mode switches.")
    red_led.value(1)
    raise SystemExit

nfc = PN532(i2c)

try:
    nfc.SAM_configuration()
    print("[NFC] PN532 ready. Scan any card to lock or unlock.")
except PN532Error as e:
    print("[ERR] SAM config failed:", e)
    raise SystemExit


last_trigger = time.ticks_ms()

while True:
    try:
        uid = nfc.read_passive_target(timeout_ms=300)
    except PN532Error as e:
        print("[ERR] Read error:", e)
        time.sleep_ms(500)
        continue

    now = time.ticks_ms()

    if uid and time.ticks_diff(now, last_trigger) > DEBOUNCE_MS:
        print("[NFC] UID:", " ".join("{:02X}".format(b) for b in uid))
        toggle_lock()
        last_trigger = now

    time.sleep_ms(SCAN_MS)
