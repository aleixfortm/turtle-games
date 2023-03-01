from turtle import Screen
import scoreboard
from snake import *
from food import *
import time

# TODO 1: CREATE OBJECT SNAKE
# TODO 2: CREATE OBJECT FOOD
# TODO 3: CREATE OBJECT SCREEN

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = scoreboard.Scoreboard()

screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    snake.move()
    screen.update()

    # Detect snake/food collision
    if snake.squares[0].distance(food) < 15:
        food.spawn()
        snake.add_square()
        scoreboard.increase_score()

    # Detect snake/wall collision
    if abs(snake.squares[0].xcor()) > 280 or abs(snake.squares[0].ycor()) > 280:
        game_is_on = False
        scoreboard.game_over()

    # Detect snake/snake collision
    for square in range(1, len(snake.squares)):
        if snake.squares[0].distance(snake.squares[square]) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
