from turtle import colormode, Turtle, Screen
import random


timmy = Turtle()
timmy.shape('turtle')
timmy.color('darkgoldenrod2')
timmy.turtlesize(3,3,3)
colormode(255)
timmy.speed('fastest')

"""
#draw a square
for i in range(4):
    timmy.fd(100)
    timmy.left(90)

#draw dashed line
timmy.right(90)
for i in range(10):
    if i%2==0:
        timmy.fd(10)
        timmy.penup()
    else:
        timmy.fd(10)
        timmy.pendown()

timmy.fd(100)
timmy.right(270)
timmy.bk(75)
timmy.clear()


# draw shapes
for i in range(3,11):
    for j in range(i):
        timmy.fd(150)
        timmy.left(360/i)

timmy.home()
timmy.clear()


# random walk

directions = [0, 90, 180, 270]
rgb = range(1,255)
timmy.pensize(15)
timmy.speed('fastest')
timmy.shapesize(1)


def rand_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return [r, b, g]


for _ in range(200):
    timmy.color(rand_color())
    timmy.fd(30)
    timmy.setheading(random.choice(directions))
    
"""

#spirograph
for i in range(90):
    timmy.circle(100)
    timmy.left(4)

screen = Screen()

screen.exitonclick()