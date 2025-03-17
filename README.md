# EMR-Services-Lights---Sirens

Welcome, Today I am here to show case my new micro-controller project “Emergency Services - Lights & Sirens” with the Raspberry PICO . 

Buzzer(Requires Sound ON)

POLICE CAR. 
AMBULANCE. 
FIRE ENGINE. 

The project is designed to emit the corresponding lights and sirens to the appropriate emergency services vehicle.
In this project Police, Medics, Firefighters all have a union to alert and make there presence noticeable for civilians and the general public of there coming and going.

With the PICO being powered by a battery pack which generates power to the PICO. I used Python  programming  to read the input data of the buttons, so that when a specific button is pressed, it would then relate back to the PICO to run a ‘while loop for each ‘if’ or ‘elif’ statement, the big RED  button represents cancel/reset. As it is programmed to ‘break’ the loop so that another button’s input can be processed when restarting the cycle.

<br>
<b>Hardware Requirements:</b>
<ul>
<img align="right" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjEnWJpbTcO-sJU5no65Hrhvb4nkBJPfLrqPnocyUqgjDbI73hE74UMNqy5RkIO4IWcttuTFEcr4PioLZhNf9JE50XHHg3YCdjNhM94x7bXTJdWXWuA8R8c9hs3XvNW5az2hNb2ptnDw/s1600/pilogo.gif" />
  <li>1x Raspberry Pi PICO</li>
  <li>1x SunFounder Breadboard Power Bank (Power Supply Module)</li>
  <li>1x Small Breadboard</li>
  <li>2x Medium Breadboard</li>
  <li>4x RED LED</li>
  <li>2x GREEN LED</li>
  <li>2x BLUE LED</li>
  <li>1x Buzzer</li>
  <li>4x Buttons</li>
  <li>10x Dupont Line</li>
  <li>10x Male-Male short line</li>
</ul>
<br>
<p>
<b>Port connection:</b> 

PICO W | LED1-RED | LED2-BLUE | LED3-GREEN | LED4-BLUE | LED5-RED | LED6-RED | BUTTON 1 | BUTTON 2 | BUTTON 3 | BUTTON 4 | BUZZER |
--- | --- | --- | --- |--- | --- | --- | --- | --- | --- | --- | --- |
GP0 | L1 |   |   |   |   |   |   |   |   |   |   |
GP1 |   | L2 |   |   |   |   |   |   |   |   |   |  
GP2 |   |   | L3 |   |   |   |   |   |   |   |   |  
GP3 |   |   |   | L4 |  |   |   |   |   |   |   |  
GP4 |   |   |   |   | L5 |  |   |   |   |   |   |  
GP5 |   |   |   |   |   | L6 |   |   |   |   |   |  
GP10 |   |   |   |   |   |   | BT1 |   |  |   |   | 
GP11 |   |   |   |   |   |   |   |  BT2 |   |  |   |
GP12 |   |   |   |   |   |   |   |   |  BT3 |   |  |
GP14 |   |   |   |   |   |   |   |   |   | BT4 |  |
GP15 |   |   |   |   |   |   |   |   |   |  | Buz |
GND | - | - | - | - | - | - | - | - | - | - | - |

</p>
