# RFID Drawer Lock

A compact NFC controlled drawer lock for when you want privacy without keys, padlocks, or drilling holes in furniture. Tap a card, the servo pulls the latch; tap again, it locks.

---

## What it does

- Tap an NFC card or tag to unlock the drawer.
- Tap again to lock it.
- Green LED shows the system is powered and ready.
- Red LED shows the drawer is locked or a card was rejected.
- Runs from a single 1S LiPo so there are no cables inside the drawer.
- Charges over USB through a TP4056 module.
- Slide switch lets you hard cut power when you do not need it.

---

## How it works

The ESP32 C3 reads the card UID from the PN532 over I²C, compares it to a stored UID, and moves the SG90 servo to either the locked or unlocked position.

```text
LiPo Battery
     ↓
TP4056 Charger   ←  USB in
     ↓
Slide Switch
     ↓
ESP32-C3-DevKitM-1
     ↓           ↓           ↓
PN532 NFC     SG90 Servo   Status LEDs
```

On first boot you register a card using the on board button. After that, only that card (or any UIDs you add in firmware) can move the servo.

---

## Hardware overview

### Main parts

| Part                     | Role                               |
|--------------------------|------------------------------------|
| ESP32 C3 DevKitM 1       | Brain of the lock                  |
| PN532 NFC module         | Reads NFC cards and tags           |
| SG90 micro servo         | Moves the latch mechanism          |
| TP4056 charging module   | Charges the 1S LiPo over USB       |
| 1S LiPo battery          | Power source                       |
| JST PH 2 pin connector   | Battery connection                 |
| Slide switch             | Main power on or off               |
| Green and Red LEDs       | Status indicators                  |
| 330 Ω resistors ×2       | LED current limiting               |

Total cost is under about 15 USD if you order parts from AliExpress.

---

## PCB

The custom PCB holds the ESP32 C3 module, status LEDs, power switch, and headers for the off board modules (PN532, TP4056, servo, and battery).

```text
Top view:
- U1: ESP32 C3 DevKitM 1 footprint
- J_NFC: 4 pin header for PN532 (I²C)
- J_SERVO: 3 pin header for SG90
- J_TP: 5 pin header for TP4056
- J_BAT: 2 pin JST PH for LiPo
- D1 / D2: Red and green LEDs
- SW3: Slide power switch
```

Place the PCB so the slide switch and LEDs line up with the cut outs in the printed enclosure.

---

## Wiring

### ESP32 C3 pinout

| Signal       | ESP32 C3 Pin |
|------------- |-------------|
| PN532 SDA    | GPIO 6      |
| PN532 SCL    | GPIO 7      |
| Servo signal | GPIO 4      |
| Red LED      | GPIO 5      |
| Green LED    | 3V3 (with resistor to GND) |

Adjust pin names in the firmware if you move any of these.

---

### Off board connections

The PCB breaks out clean headers for all off board modules. These are simple plug in connections using Dupont leads or crimped JSTs.

<details>
  <summary><strong>LiPo Battery → Battery Header (J_BAT)</strong></summary>

| Battery Wire | PCB Pin | Notes                              |
|--------------|---------|------------------------------------|
| Red (BATT+)  | Pin 1   | Positive to TP4056 B+              |
| Black (BATT−)| Pin 2   | Negative to GND and TP4056 B−      |

Use a JST PH connector, and double check polarity before plugging in. Reversing the battery can damage the TP4056 and the cell.
</details>

<details>
  <summary><strong>TP4056 Module → TP4056 Header (J_TP)</strong></summary>

| TP4056 Pin | PCB Pin | Notes                               |
|------------|---------|-------------------------------------|
| GND        | Pin 1   | Module ground                       |
| OUT+       | Pin 2   | Feeds power to the slide switch     |
| OUT−       | Pin 3   | Ground                              |
| B+         | Pin 4   | Connects to battery positive (J_BAT)|
| B−         | Pin 5   | Connects to battery negative (J_BAT)|

Plug USB into the TP4056 directly to charge the battery. Pin 6 on the header is unused.
</details>

<details>
  <summary><strong>PN532 NFC Module → NFC Header (J_NFC)</strong></summary>

| PN532 Wire | PCB Pin | Notes                          |
|------------|---------|--------------------------------|
| VCC        | Pin 1   | 3.3 V power                    |
| GND        | Pin 2   | Ground                         |
| SDA        | Pin 3   | I²C data → GPIO 6              |
| SCL        | Pin 4   | I²C clock → GPIO 7             |

Make sure your PN532 module is configured for I²C before connecting. On most boards that means both mode switches set to ON.
</details>

<details>
  <summary><strong>SG90 Servo → Servo Header (J_SERVO)</strong></summary>

| Servo Wire      | PCB Pin | Notes                                 |
|-----------------|---------|---------------------------------------|
| Brown (GND)     | Pin 1   | Ground                                |
| Red (VCC)       | Pin 2   | 5 V from the switched power rail      |
| Orange (Signal) | Pin 3   | PWM signal from GPIO 4                |

The servo runs from the 5 V switched rail, not from 3.3 V. Running it from 3.3 V will make it weak and unreliable.
</details>

---

## Enclosure and mechanics

The whole assembly is designed to work in a tight drawer, with no drilling into the furniture itself.

### Mounting the enclosure

- The main body of the enclosure sticks to the inside wall of the drawer using strong double sided tape or mounting squares.
- The PN532 sits behind a thin printed window in the front facing wall, so you can tap a card from outside the drawer.
- Screws go only into plastic parts, not into the drawer.

### Securing the servo

Inside the enclosure, the SG90 sits in a printed pocket and is clamped down by a separate bracket.

- Drop the servo into the recess so its shaft points toward the printed latch arm.
- Place the U shaped bracket over the top of the servo.
- Use two small self tapping screws (for example 2.5 to 3 mm plastic screws) from above to fasten the bracket into the printed bosses.
- Once tightened, the servo cannot move or jump out even if the drawer is slammed.

The servo horn is then screwed onto the servo shaft as normal and bolts to the printed latch arm.

### Screwing down the lid

The lid is a separate CAD part that closes the enclosure.

- After wiring everything and testing, place the lid over the base.
- Line up the four corner holes in the lid with the matching bosses in the base.
- Drive four self tapping screws straight down into the bosses until the lid is snug. Do not overtighten to avoid cracking PLA.
- The grille and LED cut outs line up with the PCB LEDs and switch so you can see status and reach the power switch with the lid installed.

With the lid screwed down and the servo clamp in place, the whole unit behaves like a single solid module that you can stick into the drawer.

---

## Building it yourself

1. **Order the parts**  
   Everything is listed in `bom/` with links. Nothing exotic.

2. **Get the PCB made**  
   Send the files in `gerbers/` to JLCPCB or PCBWay. Use standard 2 layer FR 4, 1.6 mm thickness, default stack up.

3. **Print the enclosure**  
   - STEP and STL files are under `cad/`.  
   - Print in PLA at 0.2 mm layer height.  
   - No supports are required.

4. **Solder and assemble**  
   - Solder the pin headers and connectors onto the PCB.  
   - Plug in the PN532, servo, and TP4056 using their headers.  
   - Connect the LiPo via the JST PH connector.  
   - Drop the servo into its pocket, screw down the bracket, then screw the lid to the base.

5. **Flash the firmware**

   ```bash
   git clone https://github.com/yourusername/rfid-drawer-lock
   cd rfid-drawer-lock/firmware
   # Open in Arduino IDE or PlatformIO
   # Board: "ESP32C3 Dev Module"
   # Flash and open the serial monitor
   ```

6. **Register your card**

   - On first boot, hold the register button on the PCB.  
   - Tap your NFC card on the drawer front.  
   - The green LED will blink twice to confirm the UID is saved.

7. **Mount it in the drawer**

   - Clean the inside wall of the drawer with isopropyl alcohol.  
   - Stick the enclosure in place with strong double sided tape so the PN532 window is flush with the drawer front.  
   - Close the drawer, tap your card from the outside, and watch the latch move.

---

## Customizing

- **Use a different card** – Hold the register button and tap a new card, or change the UID in firmware.
- **Allow multiple cards** – Extend the UID list in the firmware to accept several cards or tags.
- **Adjust servo angles** – Tune the open and close angles in code to match your drawer geometry and latch travel.
- **Add Wi Fi logging** – The ESP32 C3 has Wi Fi built in, so you can log open and close events to a server or MQTT broker.
- **Change indicators** – Swap LED colours or add a buzzer for audio feedback.

---

## Notes

This is a "keep people out of my drawer" project, not a high security safe. Do not rely on it to protect valuables, it is meant as a fun, practical embedded project that avoids keys and makes your drawer feel a bit smarter.
