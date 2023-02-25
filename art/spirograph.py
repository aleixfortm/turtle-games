from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

screen.colormode(255)
timmy.pensize(2)

def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


times = 60            # amount of circles to be painted (density)
radius = 150
timmy.speed(0)
angle = int(360 / times)

for _ in range(times):
    r, g, b = generate_color()
    timmy.pencolor(r, g, b)

    timmy.circle(radius)
    timmy.left(angle)

screen.exitonclick()