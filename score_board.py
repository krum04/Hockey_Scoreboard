from digits import digitRef
import machine
import neopixel


class ScoreDisplay(object):

    def __init__(self, pin):
        self.score = 0
        self.pin = pin
        self.np = neopixel.NeoPixel(machine.Pin(self.pin), 17)

        for n in range(16):
            self.np[n] = (255, 255, 255)
        self.np.write()

    def increase_score(self):
        self.score += 1
        for n in digitRef[self.score]:
            self.np[n] = (255, 255, 255)
        self.np.write()
        print('ok')


print('Home Score:')
home = ScoreDisplay(3)
for i in range(5):
    home.increase_score()

print('Away Score: ')
away = ScoreDisplay(4)
for i in range(9):
    home.increase_score()
