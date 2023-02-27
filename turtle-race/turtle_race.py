from turtle import Turtle, Screen
import random
import time

# Screen setup
screen = Screen()
screen.title('Turtle race')
screen.tracer(0)
screen.bgcolor('beige')
width = 500
height = 400
screen.setup(width=width, height=height)
screen.setworldcoordinates(0, -200, width, 200)

# Turtles setup, object assignment
turtle1 = Turtle()
turtle2 = Turtle()
turtle3 = Turtle()
turtle4 = Turtle()
turtle5 = Turtle()
drawer = Turtle()
drawer2 = Turtle()

drawer.hideturtle()
drawer2.hideturtle()

def start_finish_lines():
    # Finish line
    drawer.speed(0)
    drawer.penup()
    drawer.setpos(460, 180)
    drawer.write('Finish', font= ('Verdana', 14, 'normal'), align='center')
    drawer.setpos(460, 170)
    drawer.right(90)
    drawer.pencolor('black')
    drawer.width(3)
    drawer.pendown()
    drawer.forward(450)

    # Start line
    drawer.penup()
    drawer.setpos(50, 180)
    drawer.write('Start', font=('Verdana', 14, 'normal'), align='center')
    drawer.setpos(50, 170)
    drawer.pencolor('black')
    drawer.width(3)
    drawer.pendown()
    drawer.forward(450)

def init_pos(turtle_num):                          # Sets initial positions for each turtle
    increment = width / (len(turtles) + 1)
    x_position = (turtle_num + 1) * increment
    return x_position

def set_button_area(x_pos):                        # Sets each turtle as a clickable entity
    min_x = x_pos - 10
    min_y = -10
    max_x = x_pos + 10
    max_y = 10
    return {'min_x': min_x,
            'min_y': min_y,
            'max_x': max_x,
            'max_y': max_y}

def wait_for_click():
    global click
    screen.update()
    click = False
    while not click:
        screen.update()
    click = False

def turtle_selection(x, y):
    global selection
    global click

    click = True
    for i in range(0, len(sel_area)):
        if sel_area[i]['min_x'] < x < sel_area[i]['max_x'] and sel_area[i]['max_y'] > y > sel_area[i]['min_y']:
            selection = turtle_colors[i]

def write_init_text():
    drawer.penup()
    drawer.setpos(250, 100)
    drawer.write('Click a turtle to start!', font=('Verdana', 20, 'bold'), align='center')

def write_line_text():
    drawer.penup()
    drawer.setpos()

def game_pos():
    iteration = 1
    position = 130
    increment = 350 / len(turtles)
    for turtle in turtles:
        turtle.setx(20)
        turtle.sety(position)
        turtle.right(90)

        position -= increment
        iteration += 1

    screen.update()
    screen.tracer(1)

def draw_final_text(winner, won):
    drawer.penup()
    drawer.setpos(250, 100)
    if won:
        drawer.write(f'{winner.title()} is the winner.\nYou won!\n\nClick to exit.', font=('Verdana', 15, 'bold'),
                     align='center')
    else:
        drawer.write(f'{winner.title()} is the winner.\nYou lost...\n\nClick to exit.', font=('Verdana', 15, 'bold'),
                     align='center')
    drawer.setpos(60, 170)

def countdown():
    screen.tracer(0)
    drawer2.penup()
    drawer2.setpos(250, 0)
    num = 3
    for _ in range(3):
        drawer2.clear()
        drawer2.write(f'{num}', align='center', font=('Arial', 90, 'bold'))
        screen.update()
        time.sleep(1)
        num -= 1

    drawer2.clear()
    screen.tracer(1)

turtles = [turtle1, turtle2, turtle3, turtle4, turtle5]
turtle_colors = ['red', 'blue', 'green', 'purple', 'orange']

sel_area = []
selection = 'Out of range'
click = False

# Set up each turtle individually
for turtle_number in range(0, len(turtles)):
    each_turtle = turtles[turtle_number]
    color = turtle_colors[turtle_number]
    # Attribute assignment
    each_turtle.speed(0)
    each_turtle.shape('turtle')
    each_turtle.shapesize(1.5, 1.5)
    each_turtle.color(color)
    each_turtle.left(90)
    each_turtle.penup()
    # Set initial position
    x_init_pos = init_pos(turtle_number)
    each_turtle.setx(x_init_pos)
    # Add dictionary entry
    sel_area.append(set_button_area(x_init_pos))
    each_turtle.sety(0)

screen.update()
write_init_text()
screen.onclick(turtle_selection)

while True:
    wait_for_click()
    if selection != 'Out of range':
        break

game_pos()
drawer.clear()
start_finish_lines()
countdown()

race_ongoing = True
winner = None
while race_ongoing:
    for turtle in turtles:
        turtle.speed(1)
        turtle.forward(random.randint(0, 20))
        if turtle.xcor() >= 437:
            winner = turtle.pencolor()
            race_ongoing = False
            break

draw_final_text(winner, winner == selection)

screen.exitonclick()