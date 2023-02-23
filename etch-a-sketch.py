from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

screen.listen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def clear_screen():
    screen.reset()

screen.onkeypress(move_forwards, 'w')
screen.onkeypress(move_backwards, 's')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')
screen.onkeypress(clear_screen, 'c')

screen.exitonclick()