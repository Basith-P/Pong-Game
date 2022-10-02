import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-370, 0)
r_paddle = Paddle(370, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_game_over = False

while not is_game_over:
    screen.update()
    ball.move()
    time.sleep(.08)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(l_paddle) < 50 and ball.xcor() < -290) or (ball.distance(r_paddle) < 50 and ball.xcor() > 290):
        ball.bounce_x()

    if (ball.xcor() < -400):
        ball.reset()
        ball.bounce_x()
        scoreboard.l_point()

    if (ball.xcor() > 400):
        ball.reset()
        ball.bounce_x()
        scoreboard.r_point()

screen.exitonclick()
