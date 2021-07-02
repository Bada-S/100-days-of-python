from turtle import Turtle
ALIGNMENT = 'Center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def left_score(self):
        self.l_score += 1

    def right_score(self):
        self.r_score += 1

    def write_score(self):
        self.write(f'Player 1: {self.l_score}    Player 2: {self.r_score}', align=ALIGNMENT, font=FONT)

    def win_game(self, player):
        self.goto(0, 0)
        self.write(f'Player {player} wins. Game Over!', align=ALIGNMENT, font=FONT)
