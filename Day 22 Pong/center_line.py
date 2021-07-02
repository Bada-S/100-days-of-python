from turtle import Turtle


class CenterLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color('White')
        self.hideturtle()
        self.draw_center()

    def draw_center(self):
        self.penup()
        self.goto(0, -300)
        self.left(90)
        while self.ycor() < 300:
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)
