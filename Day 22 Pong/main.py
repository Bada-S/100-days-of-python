from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from center_line import CenterLine
import time

screen = Screen()
screen.bgcolor('black')
screen.screensize(800, 600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
center_line = CenterLine()

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

    # detects when ball either hits paddle or misses
    if abs(ball.xcor()) > 340:
        if ball.distance(r_paddle) < 50:
            ball.paddle_bounce()

        elif ball.distance(l_paddle) < 50:
            ball.paddle_bounce()
        else:
            if ball.xcor()>0:
                scoreboard.left_score()
                scoreboard.clear()
                scoreboard.write_score()
            else:
                scoreboard.right_score()
                scoreboard.clear()
                scoreboard.write_score()
            ball.reset()

    # games ends when a player wins
    if scoreboard.l_score == 11:
        scoreboard.clear()
        center_line.clear()
        ball.clear()
        scoreboard.win_game('1')
        break
    elif scoreboard.r_score == 11:
        scoreboard.clear()
        center_line.clear()
        ball.clear()
        scoreboard.win_game('2')
        break

screen.exitonclick()
