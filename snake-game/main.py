from turtle import Turtle, Screen
from snake import *
import time

# TODO 1: CREATE OBJECTS --> SNAKE, SCREEN AND FOOD

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkeypress(snake.left_prov(), 'd')
screen.onkeypress(snake.add_square(), 'c')
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move_tail()
    snake.move_forward()

screen.exitonclick()