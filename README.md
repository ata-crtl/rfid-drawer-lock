# rfid-drawer-lock
My project is a drawer lock with special dimmensions as I have a wierd drawer.
It doesnt use any screws as i canot afford to drill into the drawer, so every thing is held together by adhesive strips. 
Basically it opens the latch when ever it detects any nfc source near, the range might be a bit short due to the thickness of wood.
The reason it exists so that i can keep my belongings secure with out going throught the trouble of having my keys lost / stolen.
Say for example any nfc card / phone can be tapped  and it will open the latch, Tap agin and it will close it. i have not made a white list for which ones are allowed but if someone wants they can make that.
                     Remeber to have the nfc module up aginst the wall.
                     
step 1 . place the pinion in the engraved area and place the gear above it on the rod coming out.

step 2. attach all the wiring to the componets, make sure the lipo battery is charged

step 3 . place the motor like shown in the  photos above remebering to apply the adhesive strip under it.

step 4 . place the rfid componet against the drawer, but frist test to see if it works, if so then attach all all the components to the drawre and test it again.


onshape link = https://cad.onshape.com/documents/10ff17bd51048845f2315452/w/f69d7bc4221a2a5968c6b8fb/e/c57b2dc210264a0650e04200



<img width="492" height="727" alt="image" src="https://github.com/user-attachments/assets/f769ca3e-cc4c-4816-a1f2-bf4635f84afb" />



**All code is in micrpopython**

**SCHEMATICS**
| esp32  | 9g SG90 |
| ------------- | ------------- |
| GND | GND |
| vin  | vcc  |
| gpio 13 | signal

|esp32 | pn53 |
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

<img width="1072" height="660" alt="image" src="https://github.com/user-attachments/assets/afe1f95f-f0ba-45f3-ade6-02342ef7e973" />
<img width="3507" height="2480" alt="image" src="https://github.com/user-attachments/assets/fde249c5-b53f-4b88-ace4-086fa4f0f500" />

<img width="1067" height="573" alt="image" src="https://github.com/user-attachments/assets/8ab7b69d-2014-4c68-9408-0677734d4523" />
<img width="877" height="448" alt="Screenshot 2026-04-11 090117" src="https://github.com/user-attachments/assets/7f4565c1-eca5-48d5-8c2e-095fac5fc983" />
<img width="1601" height="584" alt="Screenshot 2026-04-11 085947" src="https://github.com/user-attachments/assets/a49dd111-f78f-4d7d-a6b1-1d93e363a5a5" />


