from turtle import *
from blocks import Block
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')
block = Block()
SFILE = "D:\Zohaib Tahir\PyCharm Project\Breakout Game\highscore.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(SFILE, "a+") as file:
            try: 
                self.highscore = int(file.read())
            except:
                self.highscore = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 280)
        self.increase_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}, High Score: {self.highscore} ', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        global block
        for block in block.block_list:
            if block in block.block_list:
                if block in block.easy_block_list:
                    self.score += 1
                elif block in block.medium_block_list:
                    self.score += 2
                elif block in block.hard_block_list:
                    self.score += 5
                elif block in block.top_block_list:
                    self.score += 10
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(SFILE, mode='w') as file:
                file.write(f'{self.highscore}')
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


class Life(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 5
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(300, 280)
        self.lose_life()
        self.update_life()

    def update_life(self):
        self.clear()
        self.write(f'Lives: {self.count}', font=FONT)

    def lose_life(self):
        self.count -= 1
        self.update_life()
