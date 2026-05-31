# RFID Drawer Lock

A compact NFC controlled drawer lock for when you want privacy without keys, padlocks, or drilling holes in furniture. Tap a card, the servo pulls the latch; tap again, it locks.

ONSHAPE LINK=https://cad.onshape.com/documents/10ff17bd51048845f2315452/w/f69d7bc4221a2a5968c6b8fb/e/c57b2dc210264a0650e04200?renderMode=0&uiState=6a1b3afc93bd5ce1c5f2ef79

---
<img width="359" height="684" alt="image" src="https://github.com/user-attachments/assets/b4b99f5a-1a05-45c1-9468-d03832a1b9c6" />


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

- The main body of the enclosure sticks to the inside wall of the drawer using strong double sided tape.
- The PN532 gets attached via adhesive strips to the back of the wall.
- Screws go only into plastic parts, not into the drawer.

### Securing the servo

Inside the enclosure, the SG90 sits in a printed pocket and is clamped down by a separate bracket.

- Drop the servo into the raised platform so its shaft points toward the gear.
- Place the U shaped bracket over the top of the servo.
- Use two small self tapping screws  from below to fasten the bracket into the printed bosses.
- Once tightened, the servo cannot move or jump out even if the drawer is slammed.

- After wiring everything and testing, place the lid over the base.
- Line up the four corner holes in the lid with the matching bosses in the base.
- Drive four self tapping screws straight down until tight.

With the lid screwed down and the servo clamp in place, the whole unit behaves like a single solid module that you can stick into the drawer.



## Building it yourself


1. **Solder and assemble**  
   - Solder the pin headers and connectors onto the PCB.  
   - Plug in the PN532, servo, and TP4056 using their headers.  
   - Connect the LiPo via the JST PH connector.  
   - Drop the servo into its pocket, screw down the bracket, then screw the lid to the base.

2. **Flash the firmware**

   ```bash
   git clone https://github.com/yourusername/rfid-drawer-lock
   cd rfid-drawer-lock/firmware
   # Open in Arduino IDE or PlatformIO
   # Board: "ESP32C3 Dev Module"
   # Flash and open the serial monitor
   ```

3. **Register your card**

   - On first boot, hold the register button on the PCB.  
   - Tap your NFC card on the drawer front.  
   - The green LED will blink twice to confirm the UID is saved.

4. **Mount it in the drawer**

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

