## Wiring

| ESP32 | SG90 Servo |
|-------|------------|
| GND   | GND        |
| VIN   | VCC        |
| GPIO 13 | Signal   |

| ESP32 | PN532 (NFC) |
|-------|-------------|
| D21   | SDA         |
| D22   | SCL         |
| 3V3   | VCC         |
| GND   | GND         |

| TP4056 | LiPo      |
|--------|-----------|
| B+     | Positive  |
| B-     | Negative  |

| TP4056      | Buck Converter |
|-------------|----------------|
| OUT+        | VIN-           |
| OUT-        | VIN+           |
