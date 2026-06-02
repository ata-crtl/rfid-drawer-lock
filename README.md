# RFID Drawer Lock

A simple NFC drawer lock made with an ESP32-C3, PN532 NFC reader and an SG90 servo.

I made this because I wanted a lockable drawer without having to use keys or drill holes into furniture. Tap an authorised NFC card and the drawer unlocks. Tap again and it locks.

**Onshape CAD**

https://cad.onshape.com/documents/10ff17bd51048845f2315452/w/f69d7bc4221a2a5968c6b8fb/e/c57b2dc210264a0650e04200

---

<img width="411" height="586" alt="Screenshot 2026-06-01 223042" src="https://github.com/user-attachments/assets/ecabc02c-fc4f-4b05-a81c-cce5e2e75a1d" />

## What it does

* Unlocks a drawer using an NFC card or tag
* Locks again when the card is tapped a second time
* Battery powered, so no cables running into the drawer
* Charges through USB using a TP4056 module
* Red and green LEDs show status
* Has a switch to completely turn the system off

---

## How it works

The PN532 reads the UID from an NFC card.

The ESP32-C3 checks whether that UID matches the stored one. If it does, the SG90 servo moves the locking mechanism.

A button is included so you can register a card when setting it up.

---

## Hardware

<img width="14030" height="9923" alt="image" src="https://github.com/user-attachments/assets/2ddba26a-29d7-4dce-9cc4-513a62371cd2" />

### Parts Used

| Part                | Purpose                |
| ------------------- | ---------------------- |
| ESP32-C3 DevKitM-1  | Main controller        |
| PN532 NFC Module    | Reads NFC cards        |
| SG90 Servo          | Moves the lock         |
| TP4056 Module       | Charges the battery    |
| 1S LiPo Battery     | Power source           |
| Slide Switch        | Power on/off           |
| Red LED             | Locked/error indicator |
| Green LED           | Power indicator        |
| 330Ω Resistors (x2) | LED current limiting   |

---

## Wiring

| Connection   | ESP32 Pin |
| ------------ | --------- |
| PN532 SDA    | GPIO 6    |
| PN532 SCL    | GPIO 7    |
| Servo Signal | GPIO 4    |
| Red LED      | GPIO 5    |

The green LED is connected to the power rail through a resistor.

Make sure the PN532 is set to **I²C mode** before connecting it.

---

## Building

### 1. Assemble the Hardware

* Solder headers and connectors onto the PCB
* Connect the PN532 module
* Connect the servo
* Connect the TP4056 charger
* Plug in the battery
* Install everything into the printed enclosure

### 2. Upload the Firmware

```bash
git clone https://github.com/yourusername/rfid-drawer-lock
cd rfid-drawer-lock
```

Open the project in Arduino IDE or PlatformIO and upload it to the ESP32-C3.

### 3. Register a Card

* Hold the register button
* Tap your NFC card
* Wait for confirmation
* The card can now lock and unlock the drawer

---

## Installation

The enclosure is designed to stick to the inside of a drawer using strong double-sided tape.

The NFC reader can be mounted behind the drawer front so cards can be scanned from outside.

No modifications to the furniture should be needed.

---

## Things I'd Like to Add Later

* Multiple authorised cards
* Wi-Fi logging
* Battery level monitoring
* Better enclosure design
* Buzzer feedback
* Mobile app support

---

## Notes

* Double-check battery polarity before connecting it.
* The servo should be powered from 5V, not 3.3V.
* Some PN532 boards ship in SPI mode by default, so check the switches/jumpers first.

---

This project was mainly built as a learning project and as a practical way to add a lock to a drawer without using traditional keys.
