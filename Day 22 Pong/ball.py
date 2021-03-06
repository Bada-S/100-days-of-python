from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(.5, .5)
        self.x_move = 3.5
        self.y_move = 3.5
        self.start = 1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def reset(self):
        if self.start == 1:
            self.goto(0, 300)
            self.y_move = -3.5
            self.start = 0
        else:
            self.goto(0, -300)
            self.y_move = 3.5
            self.start = 1
