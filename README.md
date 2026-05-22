# rfid-drawer-lock**






This project is a  RFID drawer lock with special dimensions due to having a weird drawer model .Don't mind the weird arrangement and lack of cover as space is constricted.
It doesn't use any screws as I cannot afford to drill into the drawer, so everything is held together by adhesive strips.


Additionally , because of the restricted space , a lid is not possible as it is made with a 2 mm error radius.
Basically it opens the latch whenever it detects any nfc source near, the range might be a bit short due to the thickness of wood.
The reason it exists is so that I can keep my belongings secure without going through the trouble of having my keys lost / stolen.
Say for example any nfc card / phone can be tapped  and it will open the latch, Tap again and it will close it. I have not made a white list for which ones are allowed but if someone wants they can make that.
             AND        Remember to have the nfc module up against the wall.


      
   <img width="492" height="727" alt="image" src="https://github.com/user-attachments/assets/f769ca3e-cc4c-4816-a1f2-bf4635f84afb" />      

         
Step 1 . place the pinion in the engraved area and place the gear above it on the rod coming out.


Step 2. attach all the wiring to the components, make sure the lipo battery is charged


Step 3 . place the motor like shown in the  photos below remembering to apply the adhesive strip under it.


Step 4 . place the rfid component against the drawer, but first test to see if it works, if so then attach all all the components to the drawer and test it again.



onshape link = https://cad.onshape.com/documents/10ff17bd51048845f2315452/w/f69d7bc4221a2a5968c6b8fb/e/c57b2dc210264a0650e04200?renderMode=0&uiState=6a10c880a178d4b42b3421c1




<img width="877" height="448" alt="Screenshot 2026-04-11 090117" src="https://github.com/user-attachments/assets/7f4565c1-eca5-48d5-8c2e-095fac5fc983" />
<img width="976" height="459" alt="Screenshot 2026-05-21 224850" src="https://github.com/user-attachments/assets/e53190d8-9cf6-4044-899d-2b64d7e46cbf" />
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

<img width="1328" height="511" alt="image" src="https://github.com/user-attachments/assets/9b8ba526-6064-45fa-adba-47be433c8623" />


