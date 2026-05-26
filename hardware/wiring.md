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
<img width="3507" height="2480" alt="Assembly photo 2" src="https://github.com/user-attachments/assets/fde249c5-b53f-4b88-ace4-086fa4f0f500" />
