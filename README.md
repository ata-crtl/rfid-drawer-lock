# RFID Drawer Lock

A custom RFID controlled drawer lock built to fit a very awkward real world constraint: a tight drawer space, no drilling, no screws, and only a tiny margin for print error. Because of that, the whole mechanism is held together with adhesive strips, which made it possible to keep the design compact and non-destructive.

Tap any NFC card or phone and the latch opens. Tap again and it closes. The system is simple, practical, and designed to keep contents secure without relying on keys.

> Make sure the NFC module is flush against the drawer wall, since the read range is limited by the wood thickness.

## Why I Made It

The main goal was to make a lock that works in a cramped drawer without damaging it. I wanted something that was easy to use, quick to open, and didn't require carrying around a physical key.

## Features

- RFID/NFC based unlocking.
- Tap once to open, tap again to close.
- Compact design for tight spaces.
- No drilling or screws required.
- Adhesive-mounted construction.
- ESP32-based control system.
- Rechargeable power system.

## Main Build Preview

<img width="306" height="575" alt="RFID drawer lock preview" src="https://github.com/user-attachments/assets/63f45e1e-4c5e-486a-a98b-ed9185d07583" />

## CAD

Built in Onshape — [view the model here](https://cad.onshape.com/documents/10ff17bd51048845f2315452/w/f69d7bc4221a2a5968c6b8fb/e/c57b2dc210264a0650e04200?renderMode=0&uiState=6a10c880a178d4b42b3421c1)

<img width="877" height="448" alt="CAD front" src="https://github.com/user-attachments/assets/7f4565c1-eca5-48d5-8c2e-095fac5fc983" />
<img width="976" height="459" alt="CAD side" src="https://github.com/user-attachments/assets/e53190d8-9cf6-4044-899d-2b64d7e46cbf" />

## Assembly

1. Place the pinion in the engraved area, then put the gear above it on the rod.
2. Wire everything up and make sure the LiPo is charged.
3. Mount the motor as shown in the photos below, with adhesive strip underneath.
4. Test the RFID before sticking everything down permanently. If it works, fix it all in place and test again.

<img width="1072" height="660" alt="Assembly photo" src="https://github.com/user-attachments/assets/afe1f95f-f0ba-45f3-ade6-02342ef7e973" />
<img width="3507" height="2480" alt="Assembly photo 2" src="https://github.com/user-attachments/assets/fde249c5-b53f-4b88-ace4-086fa4f0f500" />
<img width="1328" height="511" alt="Assembly photo 3" src="https://github.com/user-attachments/assets/9b8ba526-6064-45fa-adba-47be433c8623" />

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

## Notes

- The NFC module should be placed as close as possible to the drawer wall for better read performance.
- The system is intentionally simple and does not include a whitelist yet.
- Adding card filtering later would make it more secure without changing the hardware.
