


# RFID Drawer Lock

A simple NFC drawer lock built using an ESP32-C3, PN532 NFC reader, and an SG90 servo.

I made this because I wanted a way to lock a drawer without dealing with keys or drilling into furniture. Just tap an authorised NFC card to unlock it, and tap again to lock it.

**Onshape CAD**

https://cad.onshape.com/documents/10ff17bd51048845f2315452/w/f69d7bc4221a2a5968c6b8fb/e/c57b2dc210264a0650e04200

<img width="365" height="523" alt="image" src="https://github.com/user-attachments/assets/145c2482-ebe9-4971-aaad-ff4bd44a3c99" />

---

## What it does

- Unlocks a drawer using an NFC card or tag  
- Locks again when the same card is tapped  
- Runs on battery so there are no wires going into the drawer  
- Charges via USB using a TP4056 module  
- Uses red and green LEDs for status  
- Has a physical switch to turn everything off  

---

## How it works

The PN532 reads the UID from an NFC card.

The ESP32 checks if that UID matches the one stored in memory. If it matches, the SG90 servo moves the locking mechanism.

There is also a button for setup so you can register a card easily.

---

## Hardware

### Parts Used

- ESP32 DevKitM-1 for the main controller  
- PN532 NFC module for reading cards  
- SG90 servo to move the lock  
- TP4056 module for charging the battery  
- 1S LiPo battery for power  
- Slide switch for power control  
- Red LED for locked or error indication  
- Green LED for power indication  
- 330Ω resistors (x2) for LED current limiting  

---

## Wiring

- PN532 SDA  to  GPIO 6  
- PN532 SCL  to GPIO 7  
- Servo signal  to  GPIO 4  
- Red LED  to  GPIO 5  

The green LED is connected directly to the power rail through a resistor.

Make sure the PN532 is set to I2C mode before wiring it up, as some modules default to SPI.

---

## Building

### 1. Assemble the hardware

- Solder headers and connectors onto the PCB  
- Connect the PN532 module  
- Connect the servo  
- Connect the TP4056 charger  
- Plug in the battery  
- Fit everything into the 3D printed enclosure  

### 2. Upload the firmware

```bash
git clone https://github.com/yourusername/rfid-drawer-lock
cd rfid-drawer-lock
```

Open the project in Arduino IDE or PlatformIO and upload it to the ESP32.

### 3. Register a card

- Hold the register button  
- Tap your NFC card  
- Wait for confirmation  
- The card is now linked to the lock  

---

## Installation

The enclosure is designed to stick to the inside of a drawer using strong double-sided tape.

The NFC reader sits behind the drawer front so you can scan cards from outside.

No permanent modifications to the furniture are needed.
- Double check battery polarity before connecting  
- Power the servo from 5V, not 3.3V  
- Check PN532 mode (I2C vs SPI) before use  
---

## Future improvements

- Support for multiple authorised cards  
- WiFi logging  
- Battery level monitoring  
- Improved enclosure design  
- Buzzer feedback  
- Mobile app integration  



