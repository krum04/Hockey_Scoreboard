# Debug script to make sure all the leds and digits are displaying correctly

import neopixel
import machine
from time import sleep
from digits import digitRef

ledPin = 2
pixelCount = 27

np = neopixel.NeoPixel(machine.Pin(ledPin), pixelCount)
np2 = neopixel.NeoPixel(machine.Pin(14), pixelCount)

for i in range (2):
    for n in range (20):
        for i in digitRef[n]:
            np[i] = (255,0,0) 
        np.write()
        sleep(.1)
        for i in range(20):
            np[i] = (0,0,0)

for i in range (2):
    for n in range (20):
        for i in digitRef[n]:
            np2[i] = (255,0,0) 
        np2.write()
        sleep(.1)
        for i in range(20):
            np2[i] = (0,0,0)
        