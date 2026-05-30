
```markdown
#  RFID Drawer Lock

I have a drawer in my room. I wanted it locked. Not because I have anything crazy in there — I just wanted it private. A padlock felt overkill and a key is just another thing to lose. So I built this.

Tap an NFC card, drawer unlocks. Simple.

---

## What it actually does

- NFC card or tag unlocks the servo mechanism
-  Green LED tells you it's on
-  Red LED tells you it's locked or your card was rejected
- Runs on a LiPo battery so no cables needed inside the drawer
- Charges over USB via the TP4056 module
- Slide switch to cut power when you don't need it

---

## How it's built

This started on a breadboard and ended up as a custom PCB designed in KiCad. The 3D printed enclosure holds everything together and mounts cleanly inside the drawer — no screws, no drilling, just adhesive.

```

LiPo Battery
     ↓
TP4056 charger  ←  USB in
     ↓
Slide switch
     ↓
ESP32-C3-DevKitM-1
     ↓           ↓           ↓
PN532 NFC     SG90 Servo   LEDs
```

The ESP32-C3 handles everything. It reads the card UID over I2C from the PN532, checks it against the stored UID, and if it matches it drives the servo to open. Tap again and it locks back.

---

## Parts

| Part | What it does |
|------|-------------|
| ESP32-C3-DevKitM-1 | Brain of the whole thing |
| PN532 NFC module | Reads cards and tags |
| SG90 servo | Moves the lock |
| TP4056 module | Charges the battery |
| 1S LiPo battery | Keeps it wireless |
| JST-PH 2-pin connector | Battery connection |
| Slide switch | Power on/off |
| Green + Red LEDs | Status indicators |
| 330Ω resistors x2 | LED protection |

> Total cost is under $15 if you order from AliExpress.

---

## Wiring

| Signal | ESP32-C3 Pin |
|--------|-------------|
| PN532 SDA | GPIO6 |
| PN532 SCL | GPIO7 |
| Servo signal | GPIO4 |
| Red LED | GPIO5 |
| Green LED | 3V3 rail |

---

## Off Board Connections

These are the physical wires that run from the PCB headers out to each external module.

<details>
<summary><b> LiPo Battery → Battery Header (J_BAT)</b></summary>
<br>

| Battery Wire | PCB Pin | Notes |
|-------------|---------|-------|
| Red (BATT+) | Pin 1 | Positive to TP4056 B+ |
| Black (BATT-) | Pin 2 | Negative to GND |

>  Use the JST-PH connector. Do not reverse polarity — it will damage the battery and TP4056.

</details>

<details>
<summary><b> TP4056 Module → TP4056 Header (J_TP)</b></summary>
<br>

| TP4056 Pin | PCB Pin | Notes |
|------------|---------|-------|
| GND | Pin 1 | Module ground |
| OUT+ | Pin 2 | Feeds power to slide switch |
| OUT- | Pin 3 | GND |
| B+ | Pin 4 | Goes to battery positive |
| B- | Pin 5 | Goes to battery negative |

> Plug USB into the TP4056 module directly to charge. Pin 6 is left empty.

</details>

<details>
<summary><b> PN532 NFC Module → NFC Header (J_NFC)</b></summary>
<br>

| PN532 Wire | PCB Pin | Notes |
|-----------|---------|-------|
| VCC | Pin 1 | 3.3V power |
| GND | Pin 2 | Ground |
| SDA | Pin 3 | I2C data → GPIO6 |
| SCL | Pin 4 | I2C clock → GPIO7 |

> Make sure your PN532 module has its mode switches set to I2C before plugging in. On most modules that means both switches to ON.

</details>

<details>
<summary><b> SG90 Servo → Servo Header (J_SERVO)</b></summary>
<br>

| Servo Wire | PCB Pin | Notes |
|-----------|---------|-------|
| Brown (GND) | Pin 1 | Ground |
| Red (VCC) | Pin 2 | 5V from switched power rail |
| Orange (Signal) | Pin 3 | PWM signal from GPIO4 |

> The servo runs off the switched power rail, not 3.3V. If you feed it 3.3V it will be weak and unreliable.

</details>

---

## Files in this repo

```

rfid-drawer-lock/
├── kicad/          KiCad schematic and PCB layout
├── gerbers/        Ready to send to JLCPCB or PCBWay
├── cad/            3D models and STEP files for the enclosure
├── firmware/       Source code
├── bom/            Bill of materials with links
├── photos/         Build photos
└── README.md
```

---

## Building it yourself

### 1. Order the parts
Everything is in `/bom/` with links. Nothing exotic.

### 2. Get the PCB made
Send `/gerbers/` to JLCPCB or PCBWay. Standard settings — 2 layer, 1.6mm, FR4.

### 3. Print the enclosure
STEP and STL files are in `/cad/`. Printed in PLA at 0.2mm layer height. No supports needed.

### 4. Solder and assemble
Solder the pin headers onto the PCB. Plug in the modules. Connect the battery. Mount everything in the printed enclosure.

### 5. Flash the firmware

```bash
git clone https://github.com/yourusername/rfid-drawer-lock
cd rfid-drawer-lock/firmware
# Open in Arduino IDE or PlatformIO
# Board: ESP32-C3 Dev Module
# Flash and open serial monitor
```

### 6. Register your card
On first boot hold the register button and tap your card. Green LED blinks twice to confirm it saved.

### 7. Mount it
Stick it inside your drawer with double sided tape. The PN532 sits flush against the drawer front. Done.

---

## Customizing it

- **Different card** — re-register via the button or change the UID in firmware
- **Multiple cards** — extend the UID list in the code
- **Servo angles** — adjust open and close angles to fit your lock geometry
- **WiFi logging** — the ESP32-C3 has WiFi built in, easy to add if you want a log of when the drawer opened



The off board connections are inside `<details>` dropdowns so the page stays clean but everything is there when someone expands it. Just replace `yourusername` with your actual GitHub username before pasting.
