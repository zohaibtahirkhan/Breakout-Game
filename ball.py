from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -120)
        self.shape("circle")
        self.color("#fff")
        self.x_move = 3
        self.y_move = 3
        self.move()
        self.speed('fastest')
        self.bounce_x()
        self.bounce_y()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
