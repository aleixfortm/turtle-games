from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
ANGLES = [0, 90, 180, 270]

class Snake:

    def __init__(self):
        self.squares = []
        self.square_size = 20
        self.turn = None
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_square = Turtle()
            new_square.penup()
            new_square.shape()
            new_square.color('white')
            new_square.goto(position)
            self.squares.append(new_square)

    def move_tail(self):
        for i in range(1, len(self.squares)):
            self.squares[-i].setpos(self.squares[-(i + 1)].pos())

    def move_forward(self):
        self.squares[0].forward(self.square_size)

    def left_prov(self):
        self.squares[0].setheading(self.squares[0].heading() + 90)

    def turn_right(self):
        self.turn = True
        for i, angle in enumerate(ANGLES):
            if angle == self.squares[0].heading():
                self.squares[0].setheading(ANGLES[(i + 1) % 4])

    def turn_left(self):
        self.turn = False
        for i, angle in enumerate(ANGLES):
            if angle == self.squares[0].heading():
                self.squares[0].setheading(ANGLES[(i - 1) % 4])

    def new_square_position(self):
        if self.squares[0].heading() == 0:
            x = - self.square_size
            y = 0
            direction = 'right'
        elif self.squares[0].heading() == 90:
            x = 0
            y = - self.square_size
            direction = 'up'
        elif self.squares[0].heading() == 180:
            x = self.square_size
            y = 0
            direction = 'left'
        elif self.squares[0].heading() == 270:
            x = 0
            y = self.square_size
            direction = 'down'

        # noinspection PyUnboundLocalVariable
        return x, y, direction

    def add_square(self):
        new_square = Turtle()
        new_square.penup()
        new_square.color('white')
        x, y, direction = self.new_square_position()
        new_square.goto(self.squares[-1].xcor() + x, self.squares[-1].ycor() + y)
        self.squares.append(new_square)

