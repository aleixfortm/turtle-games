from turtle import Turtle

# TODO 1: ATTRIBUTES --> Square objects, square size

square_size = 20
INITIAL_SQUARES = 3

class Snake():

    def __init__(self):
        self.squares = []
        self.square_size = 20
        self.initial_squares()

    def initial_squares(self):
        for x in range(INITIAL_SQUARES):
            self.add_square()
            self.squares[-1].setpos(-20 * x, 0)

    def add_square(self):
        square = Turtle()
        square.color('white')
        square.shape('square')
        square.penup()
        self.squares.append(square)
        x_ref, y_ref = self.define_position()
        square.goto(self.squares[-1].xcor() + x_ref, self.squares[-1].ycor() + y_ref)

    def define_position(self):
        if self.squares[-1].heading() == 0:
            return -square_size, 0
        if self.squares[-1].heading() == 90:
            return 0, -square_size
        if self.squares[-1].heading() == 180:
            return square_size, 0
        if self.squares[-1].heading() == 270:
            return 0, square_size

    def move(self):
        for i in range(len(self.squares) - 1, 0, -1):
            self.squares[i].setpos(self.squares[i - 1].pos())
        self.squares[0].forward(square_size)

    def up(self):
        if self.squares[0].heading() != 270:
            self.squares[0].seth(90)

    def left(self):
        if self.squares[0].heading() != 0:
            self.squares[0].seth(180)

    def down(self):
        if self.squares[0].heading() != 90:
            self.squares[0].seth(270)

    def right(self):
        if self.squares[0].heading() != 180:
            self.squares[0].seth(0)


