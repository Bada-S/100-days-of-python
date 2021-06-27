from turtle import Turtle, Screen
import random as r

screen = Screen()
screen.setup(500, 400)

colors = ['green', 'yellow', 'orange', 'red', 'purple', 'blue']
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: "
                                                          "(green, yellow, orange, red, purple, blue)")

turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, -100 + (i * 40))
    turtles.append(new_turtle)

race = False
if user_bet:
    race = True
while race:
    for turtle in turtles:
        dist = r.randint(0,10)
        turtle.forward(dist)
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! {turtle.pencolor()} is the winner!")
            else:
                print(f"You guessed wrong. {turtle.pencolor()} is the winner")
            race = False

screen.exitonclick()
