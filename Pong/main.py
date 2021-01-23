from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("blue")
screen.screensize(canvwidth=800, canvheight=600)
screen.title("Ping-Pong")

game_is_on = True

playerA = Paddle(x_cor=-350, y_cor=0)
playerB = Paddle(x_cor=350, y_cor=0)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(playerB.go_up, "Up")
screen.onkey(playerB.go_down, "Down")
screen.onkey(playerA.go_up, "w")
screen.onkey(playerA.go_down, "s")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle.
    if (ball.xcor() >= 330 and ball.distance(playerB) < 50) or (ball.xcor() <= -330 and ball.distance(playerA) < 50):
            ball.bounce_x()

    #detect ball exit.
    if ball.xcor() > 350 :
        scoreboard.increase_score(1)
        ball.reset_position()

    if ball.xcor() < -350:
        scoreboard.increase_score(2)
        ball.reset_position()

    if scoreboard.score_p1 >= 3 or scoreboard.score_p2 >= 3:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()

