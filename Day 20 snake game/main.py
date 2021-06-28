from turtle import Screen, Turtle
import time
from snake import Snake
# snake game
# earn points be eating the food
# game over when snake collides with wall or with tail

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

while True:
    screen.update()
    time.sleep(.1)
    snake.move()

screen.exitonclick()
