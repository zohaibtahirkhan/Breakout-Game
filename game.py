from turtle import *
import time
from bloc import Paddle
from ball import Ball
from blocks import Block
import medium_block
import easy_block
import hard_block
import top_block
from scoreboard import Scoreboard, Life

screen = Screen()
screen.bgcolor("black")
screen.title("Bloc.")
screen.setup(800, 600)
screen.tracer(0)
game_is_on = True
paddle = Paddle()
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")
ball = Ball()
base_block = Block()
scoreboard = Scoreboard()
life = Life()


def blocks():
    for x in range(-360, 360, 40):
        new_block = easy_block.EasyBlock()
        new_block.goto(x, 0)
        base_block.block_list.append(new_block)
        base_block.easy_block_list.append(new_block)
        new_block = medium_block.MediumBlock()
        new_block.goto(x, 40)
        base_block.block_list.append(new_block)
        base_block.medium_block_list.append(new_block)
        new_block = hard_block.HardBlock()
        new_block.goto(x, 80)
        base_block.block_list.append(new_block)
        base_block.hard_block_list.append(new_block)
        new_block = top_block.TopBlock()
        new_block.goto(x, 120)
        base_block.block_list.append(new_block)
        base_block.top_block_list.append(new_block)


blocks()
while game_is_on:
    screen.update()
    time.sleep(0.00001)
    ball.move()

    if ball.distance(paddle) < 40:
        ball.bounce_y()
    if 370 < ball.xcor() or ball.xcor() < -370:
        ball.bounce_x()
    if 280 < ball.ycor():
        ball.bounce_y()
    for block in base_block.block_list:
        if ball.distance(block) < 20:
            block.delete_block()
            scoreboard.score += 1
            scoreboard.update_score()

    if ball.ycor() < -280:
        if life.count >= 1:
            life.lose_life()
            ball.bounce_y()
        elif life.count <= 0:
            scoreboard.game_over()
            scoreboard.reset()
            game_is_on = False
screen.exitonclick()
