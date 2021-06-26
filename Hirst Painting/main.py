import colorgram as c
import turtle as t
import random as r

""""
#Generate color list with this code
rgb_colors = []
colors = c.extract('hirst.jpg', 100)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))
"""
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]
t.colormode(255)
timmy = t.Turtle()
timmy.penup()
timmy.goto(-250,-250)
timmy.pendown()
#starting position

for j in range(10):
    for i in range(10):
        timmy.dot(20, r.choice(color_list))
        timmy.penup()
        timmy.fd(50)
        timmy.pendown()
    timmy.penup()
    timmy.setposition(-250, -250 + ((j+1) * 50))
    timmy.pendown()

screen = t.Screen()
screen.setup(700, 700)
screen.exitonclick()
