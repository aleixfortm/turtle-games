from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

screen.colormode(255)
screen.bgcolor('beige')
timmy.pensize(2)

def draw_circle(radius):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    timmy.color(color_tuple, color_tuple)
    timmy.begin_fill()
    timmy.circle(radius)
    timmy.end_fill()


radius = 30
columns = 9
lines = 5

timmy.speed(0)
timmy.penup()
timmy.setx(-400)
timmy.sety(-350)
timmy.pendown()

for line_number in range(lines):
    for column_number in range(columns):
        draw_circle(radius)
        if column_number + 1 != columns:
            timmy.penup()
            timmy.forward(100)
            timmy.pendown()

    timmy.penup()
    if line_number % 2 == 0:
        timmy.left(90)
        timmy.forward(100 + radius * 4)
        timmy.left(90)
    else:
        timmy.right(90)
        timmy.forward(100)
        timmy.right(90)
    timmy.pendown()

screen.exitonclick()
