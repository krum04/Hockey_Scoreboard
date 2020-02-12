from digits import digitRef
from time import sleep
import machine
import neopixel

# Setup our button inputs
homeButton = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
awayButton = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

# ScoreDisplay object will be created for each set of scores
# Will take team, pin number driving leds, and the number of leds


class ScoreDisplay(object):
    def __init__(self, team, pin, numLeds):
        self.team = team
        self.score = 0
        self.pin = pin
        self.np = neopixel.NeoPixel(machine.Pin(self.pin), numLeds)
        self.numLeds = numLeds

    # References the included digit module that contains display list for each number
    def increase_score(self):
        self.score += 1
        if self.score == 20:
            self.score = 0
        for n in digitRef[self.score]:
            self.np[n] = (255, 255, 255)
        self.np.write()
        print('{} Score: {}'.format(self.team, self.score))
    
    # Turn off all leds
    def clear_leds(self):
        for i in range(27):
            self.np[i] = (0,0,0)
        self.np.write()

  
  




# Create an object for each team and pass in our arguments
home = ScoreDisplay('Home', 14, 27)
away = ScoreDisplay('Away', 2, 27)

flag = True

# Monitor button change state and increse score acordingly
home.clear_leds()
away.clear_leds()

while flag:
    homeFirst = homeButton.value()
    #sleep(0.005)
    homeSecond = homeButton.value()
    if homeFirst == False:
        
        home.clear_leds()
        home.increase_score()
        sleep(.5)
    else:
        pass

    awayFirst = awayButton.value()
    #sleep(0.005)
    awaySecond = awayButton.value()
    if awayFirst == False:
        
        away.clear_leds()
        away.increase_score()
        sleep(.5)
    else:
        pass

    if not homeButton.value() and not awayButton.value():
        flag = False
