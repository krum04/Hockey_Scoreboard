# Debug script to make sure all the leds and digits are displaying correctly

import neopixel
import machine
from time import sleep
from digits import digitRef

ledPin = 0
pixelCount = 27

np = neopixel.NeoPixel(machine.Pin(ledPin)), pixelCount)

for n in range (19):
    for i in digitRef[n]:
        np[i] = (255,255,255) 
    np.write()
    sleep(1)