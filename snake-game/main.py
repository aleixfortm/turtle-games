from turtle import Screen
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

screen.exitonclick()
