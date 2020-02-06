from digits import digitRef


class ScoreDisplay(object):

    def __init__(self, pin):
        self.score = 0
        self.pin = pin
        print(self.score)

    def increase_score(self):
        self.score += 1
        for n in digitRef[home.score]:
            print(n)


home = ScoreDisplay(3)
for i in range(5):
    home.increase_score()

away = ScoreDisplay(4)
for i in range(9):
    home.increase_score()
