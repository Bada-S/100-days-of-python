from turtle import Turtle, Screen

tim = Turtle()

def move_fd():
    tim.fd(10)

screen = Screen()
screen.listen()
screen.onkey(key='space', fun=move_fd)
screen.exitonclick()