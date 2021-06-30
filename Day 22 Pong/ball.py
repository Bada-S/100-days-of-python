from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(.5, .5)

    def move(self):
        new_x = self.xcor() + 2.5
        new_y = self.ycor() + 2.5
        self.goto(new_x, new_y)
