from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('yellow')
        self.shapesize(.5, .5)
        self.speed('fastest')
        self.goto(random.randint(-250, 250), random.randint(-250, 250))

    def refresh(self):
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
