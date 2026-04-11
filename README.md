# rfid-drawer-lock
My project is a drawer lock with special dimmensions as I have a wierd drawer.
It doesnt use any screws as i canot afford to drill into the drawer, so every thing is held together by adhesive strips. 
Basically it opens the latch when ever it detects any nfc source near, the range might be a bit short due to the thickness of wood.
The reason it exists so that i can keep my belongings secure with out going throught the trouble of having my keys lost / stolen.
Say for example any nfc card / phone can be tapped  and it will open the latch, Tap agin and it will close it. i have not made a white list for which ones are allowed but if someone wants they can make that.

**SCHEMATICS**
| esp32c3  | 9g SG90 |
| ------------- | ------------- |
| GND | GND |
| vin  | vcc  |
| gpio 13 | signal

|esp32c3 | pn53 |
| --------|--------|
| d21 | SDA |
| D22 | SCL |
| 3V3 | VCC |
| GND | GND |

|tp4056 | lipo |
| --------|--------|
| B+  | POSITIVE |
| B-  | NEGATIVE  |

|tp4056 | BUCK CONVERTER |
| --------|--------|
| OUT+  | VIN - |
| OUT-  | VIN + |

