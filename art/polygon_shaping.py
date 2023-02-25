from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

def draw_shape(degrees, n_sides):
    for _ in range(n_sides):
        timmy.forward(100)
        timmy.right(180 - degrees)

def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def set_starting_pos():
    timmy.penup()
    timmy.setx(-50)
    timmy.sety(200)
    timmy.pendown()


timmy.width(2)
timmy.speed(0)

set_starting_pos()

screen.colormode(255)

sides = 3
total_degrees = 180
while sides < 15:
    angle = total_degrees / sides
    timmy.pencolor(generate_color())
    draw_shape(angle, sides)
    sides += 1
    total_degrees += 180

screen.exitonclick()