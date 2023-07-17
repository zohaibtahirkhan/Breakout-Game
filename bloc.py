from turtle import *


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -200)
        self.shape("square")
        self.color("#0000FF")
        self.shapesize(stretch_len=8)
        self.move_left()
        self.move_right()

    def move_left(self):
        if self.xcor() > -320:
            self.backward(10)

    def move_right(self):
        if self.xcor() < 320:
            self.forward(10)
