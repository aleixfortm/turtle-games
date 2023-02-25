from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def generate_angle():
    x = random.randint(0, 3)
    angle = 90 * x
    return angle


screen.colormode(255)
screen.bgcolor('black')

timmy.speed(0)
timmy.pensize(10)
timmy.color('grey')

for _ in range(100):
    r, g, b = generate_color()
    ang = generate_angle()

    timmy.pencolor(r, g, b)
    timmy.forward(30)
    timmy.right(ang)

screen.exitonclick()