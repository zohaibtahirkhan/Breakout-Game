from turtle import *


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.top_block_list = []
        self.hard_block_list = []
        self.medium_block_list = []
        self.easy_block_list = []
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=2)
        self.penup()
        self.block_list = []

    def delete_block(self):
        self.hideturtle()
