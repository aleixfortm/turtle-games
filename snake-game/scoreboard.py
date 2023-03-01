from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.display_score()

    def display_score(self):
        self.setpos(0, 270)
        self.write(f'Score: {self.score}', True, align='center', font=('Verdana', 16, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write('GAME OVER', True, align='center', font=('Verdana', 30, 'normal'))