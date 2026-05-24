# RFID Drawer Lock

A custom RFID-controlled drawer lock built around the constraints of a weirdly shaped drawer — 
no drilling, no screws, 2mm error radius on the prints. Everything is held together with 
adhesive strips because that's just how it had to be done.

Tap any NFC card or phone → latch opens. Tap again → latch closes.  
No whitelist (anyone with NFC can open it), but that's easy to add if you want it.

> Make sure the NFC module is flush against the wall of the drawer, 
> read range is a bit short due to wood thickness.

The whole point of this is to keep my stuff secure without worrying about losing keys.

<img width="435" height="702" alt="image" src="https://github.com/user-attachments/assets/14b46b2d-4369-4373-b8d3-66df6cfde8a7" />

---

## CAD

Built in Onshape — [view the model here](https://cad.onshape.com/documents/10ff17bd51048845f2315452/w/f69d7bc4221a2a5968c6b8fb/e/c57b2dc210264a0650e04200?renderMode=0&uiState=6a10c880a178d4b42b3421c1)

<img width="877" height="448" alt="CAD front" src="https://github.com/user-attachments/assets/7f4565c1-eca5-48d5-8c2e-095fac5fc983" />
<img width="976" height="459" alt="CAD side" src="https://github.com/user-attachments/assets/e53190d8-9cf6-4044-899d-2b64d7e46cbf" />

---

## Assembly

1. Place the pinion in the engraved area, then put the gear above it on the rod.
2. Wire everything up and make sure the LiPo is charged.
3. Mount the motor as shown in the photos below — adhesive strip under it.
4. Before sticking everything down, test the RFID first. If it works, fix it all in place and test again.

<img width="1072" height="660" alt="Assembly photo" src="https://github.com/user-attachments/assets/afe1f95f-f0ba-45f3-ade6-02342ef7e973" />
<img width="3507" height="2480" alt="Assembly photo 2" src="https://github.com/user-attachments/assets/fde249c5-b53f-4b88-ace4-086fa4f0f500" />
<img width="1328" height="511" alt="Assembly photo 3" src="https://github.com/user-attachments/assets/9b8ba526-6064-45fa-adba-47be433c8623" />

---

## Wiring

| ESP32 | SG90 Servo |
|-------|------------|
| GND | GND |
| VIN | VCC |
| GPIO 13 | Signal |

| ESP32 | PN532 (NFC) |
|-------|-------------|
| D21 | SDA |
| D22 | SCL |
| 3V3 | VCC |
| GND | GND |

| TP4056 | LiPo |
|--------|------|
| B+ | Positive |
| B- | Negative |

| TP4056 | Buck Converter |
|--------|----------------|
| OUT+ | VIN- |
| OUT- | VIN+ |

