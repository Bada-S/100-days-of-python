from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.screensize(800, 600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    ball.move()
    time.sleep(.01)
    screen.update()
    if abs(ball.ycor()) == 300:
        ball.bounce()

    if (abs(ball.xcor()) > 340) and ((ball.distance(r_paddle) < 50) or (ball.distance(l_paddle) < 50)):
        ball.paddle_bounce()

screen.exitonclick()
