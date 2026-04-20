# rfid-drawer-lock
My project is a drawer lock with special dimmensions as I have a wierd drawer.
It doesnt use any screws as i canot afford to drill into the drawer, so every thing is held together by adhesive strips. 
Basically it opens the latch when ever it detects any nfc source near, the range might be a bit short due to the thickness of wood.
The reason it exists so that i can keep my belongings secure with out going throught the trouble of having my keys lost / stolen.
Say for example any nfc card / phone can be tapped  and it will open the latch, Tap agin and it will close it. i have not made a white list for which ones are allowed but if someone wants they can make that.

PS---**To download the zine just press view in raw format**
<img width="773" height="1167" alt="image" src="https://github.com/user-attachments/assets/e3a52dca-2846-4ef4-b877-243123e3f29d" />


**All code is in micrpopython**
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

<img width="1067" height="573" alt="image" src="https://github.com/user-attachments/assets/8ab7b69d-2014-4c68-9408-0677734d4523" />
<img width="877" height="448" alt="Screenshot 2026-04-11 090117" src="https://github.com/user-attachments/assets/7f4565c1-eca5-48d5-8c2e-095fac5fc983" />
<img width="1601" height="584" alt="Screenshot 2026-04-11 085947" src="https://github.com/user-attachments/assets/a49dd111-f78f-4d7d-a6b1-1d93e363a5a5" />


