from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# snake game
# earn points be eating the food
# game over when snake collides with wall or with tail

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

while True:
    screen.update()
    time.sleep(.1)
    snake.move()

    #detect collision with food
    if snake.snake_body[0].distance(food) < 15:
        print('nom')
        food.refresh()
        scoreboard.score_point()

    #detect collision with outer boundaries
    head = snake.snake_body[0]
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        scoreboard.game_over()
        break

screen.exitonclick()
