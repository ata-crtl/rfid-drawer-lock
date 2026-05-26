# Automatic Door Closer

A rechargeable automatic door closer designed to solve a simple but frustrating problem: doors being left open. With a single button press, the system activates a motor-driven pulley mechanism that pulls the door shut reliably and consistently.

The project combines mechanical design, embedded control, and wireless communication. An ESP32 controls a high-power motor through a driver, while a separate remote unit allows the door to be closed from a distance. The system is built with a rechargeable power setup, making it portable and easy to maintain without constant battery replacement.

## Why I Made It

I got tired of my door constantly being left open, so I built something practical to fix it. The goal was to keep the system simple: press one button, and the door closes.

## Features

- Push-button door closing.
- High-power motor for stronger pulling force.
- Rechargeable power system.
- ESP32-based control system.
- Separate remote sender.
- Designed to mount onto a door and above the door frame.

## Important Safety Check

Before attaching the wires to the ESP32 VIN pin, use a multimeter to make sure the wire coming from the buck converter is **5V**. Do the same for the remote power output before connecting it to the ESP32.

## CAD

**Onshape link:**  
[View the Onshape model](https://cad.onshape.com/documents/bdd11de85f4570d51cb36bd7/w/b7536c01ad29c059d531be40/e/07df8b484f8b3f7ee84a2b9b?renderMode=0&uiState=6a15705f002f3bb3f2bcfc0f)

## Main Build Preview

<img width="530" height="769" alt="Main build preview" src="https://github.com/user-attachments/assets/536c9a44-3177-43e3-ab12-387108aa1cf3" />

## Bill of Materials

| Item | Notes |
|------|-------|
| ESP32 | Main controller for the door closer |
| ESP32 | Controller used in the sender remote |
| L298N motor driver | Drives the main motor |
| High-power motor | Provides the force to close the door |
| USB-C charging module | Charges the battery in the main unit |
| TP4056 charging module | Charges the battery in the remote |
| Buck converter | Steps voltage down to 5V for the ESP32 |
| Boost/step-up module | Steps voltage up for the remote ESP32 |
| Rechargeable battery | Main power source |
| Push button | Used to trigger the system |
| Fishing line | Connects the pulley system to the door |
| Screws | Used to mount the mechanism and close the case |
| Adhesive for wood | Used where needed for secure mounting |
| Multimeter | Needed to verify output voltage before wiring |

## Main Unit Connections

| Part | Pin | Connects to |
|------|-----|-------------|
| USB-C charging module | VO+ | Battery red (+) |
| USB-C charging module | VO- | Battery black (-) |
| Battery | Red (+) | Buck converter IN+ |
| Battery | Black (-) | Buck converter IN- |
| Battery | Black (-) | L298N GND terminal |
| Battery | Black (-) | USB-C module VO- |
| Buck converter | OUT+ | ESP32 VIN or 5V |
| Buck converter | OUT- | ESP32 GND |
| Battery | Red (+) | L298N 12V |
| Battery | Black (-) | L298N GND terminal |
| ESP32 | GPIO 12 | L298N IN1 |
| ESP32 | GPIO 13 | L298N IN2 |

<img width="3508" height="2480" alt="Main unit wiring diagram" src="https://github.com/user-attachments/assets/dffa8311-d884-44aa-8000-76867a76e0b3" />

## Sender Remote Connections

| Part | Pin | Connects to |
|------|-----|-------------|
| Button | Leg 1 | ESP32 GPIO 15 |
| Button | Leg 2 | ESP32 GND |
| Battery | Positive | TP4056 B+ |
| Battery | Negative | TP4056 B- |
| TP4056 | OUT+ | Boost module VIN+ |
| TP4056 | OUT- | Boost module VIN- |
| Step-up module | VOUT+ | ESP32 5V |
| Step-up module | VOUT- | ESP32 GND |

## Electronics Overview

<img width="552" height="276" alt="Electronics overview" src="https://github.com/user-attachments/assets/2daa2f66-122b-4983-a579-9aaa15454b40" />

## Assembly Instructions

### Main Mechanism

**Step 1:** Connect all the electronics.

**Step 2:** Connect these parts as shown below.

<img width="482" height="381" alt="Assembly step 2" src="https://github.com/user-attachments/assets/35f0c773-a427-409d-ba69-0411f42e06e3" />

**Step 3:** Insert the assembly into the main frame as shown.

<img width="592" height="417" alt="Assembly step 3" src="https://github.com/user-attachments/assets/775ac7c0-9169-46fa-b4eb-01dd6f7bb59e" />

**Step 4:** Insert the part shown into the pulley system, then attach the motor.

<img width="1215" height="327" alt="Assembly step 4" src="https://github.com/user-attachments/assets/5667d320-ce3b-40a8-91f3-95d18a61fdf6" />

**Step 5:** Insert the heated threaded inserts in the locations shown below.

<img width="1245" height="686" alt="Threaded inserts 1" src="https://github.com/user-attachments/assets/b287b5ce-b364-4d46-a53c-18261e3a52a8" />

<img width="941" height="716" alt="Threaded inserts 2" src="https://github.com/user-attachments/assets/4ea8070c-2e8b-46e9-83a0-7a63b88441cb" />

<img width="762" height="581" alt="Threaded inserts 3" src="https://github.com/user-attachments/assets/1ee3a7a4-246d-42ec-9731-b988ca665dbf" />

<img width="685" height="408" alt="Threaded inserts 4" src="https://github.com/user-attachments/assets/97860aa0-069a-4aa9-91e0-e87e1e553273" />

<img width="574" height="333" alt="Threaded inserts 5" src="https://github.com/user-attachments/assets/d4da18b2-169c-4a2a-9305-649a9400c707" />

**Step 6:** Secure the motor using the inserts as shown.

<img width="762" height="581" alt="Motor secured" src="https://github.com/user-attachments/assets/be93524b-bd7f-47ef-a621-e62f62c367cf" />

**Step 7:** Use three screws to secure the lid.

<img width="1332" height="540" alt="Assembly step 5" src="https://github.com/user-attachments/assets/a8847131-c2ac-43f2-a6ae-ef1f767a284e" />

**Step 8:** Secure the unit to the door using four 20 mm screws.

<img width="842" height="457" alt="Assembly step 6" src="https://github.com/user-attachments/assets/14c9a15f-8c15-404c-b9e6-f5591c0df92d" />

**Step 9:** Attach the top mount above the door using four screws.

<img width="516" height="352" alt="Assembly step 7" src="https://github.com/user-attachments/assets/5e7975af-ab9b-40c2-a3d3-26c19963dbbe" />

**Step 10:** Tie one end of the fishing line to the hole in the pulley wheel and the other end to the hook above the door.

<img width="1157" height="815" alt="Assembly step 8" src="https://github.com/user-attachments/assets/73b67b78-9201-4ae9-b1d9-ab369c6ba442" />

### Remote

**Step 1:** Put the button through the hole in the lid.

<img width="380" height="382" alt="Remote step 1" src="https://github.com/user-attachments/assets/e3373d02-2956-492f-b2d2-9bda6ebd830d" />

**Step 2:** Attach the electronics.

**Step 3:** Close the lid and screw it down using four screws.
