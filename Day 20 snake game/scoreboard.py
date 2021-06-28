from turtle import Turtle
ALIGNMENT = 'Center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.write_score()
        self.hideturtle()

    def score_point(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write('Game over!', align=ALIGNMENT, font = ('Courier', 48, 'normal'))
