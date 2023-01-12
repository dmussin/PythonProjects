from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.new_y = 0
        self.shape("turtle")
        self.color('green')
        self.setheading(90)
        self.goto(0, -260)

    def up(self):
        self.new_y = self.ycor() + 10
        self.goto(self.xcor(), self.new_y)

    def reset_position(self):
        self.goto(0,-260)
