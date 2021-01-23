from turtle import Turtle, Screen
from random import choice

def start_position(competitors):
    x_pos = -230
    y_pos = 120
    for i in range(0,len(competitors)):
        y_pos -= 20
        competitors[i][0].goto(x=x_pos,y=y_pos)

def finish_line(turtle):
    if turtle.xcor() > 220:
        return True
    else:
        return False

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
colors = ["red","green", "blue", "yellow", "purple", "pink", "orange"]
winner = ""
turtles = []
each_turtle = []
for i in range(0,len(colors)):
    each_turtle = []
    each_turtle.append(Turtle(shape="turtle"))
    each_turtle[0].penup()
    each_turtle[0].color(colors[i])
    each_turtle.append(colors[i])
    turtles.append(each_turtle)

start_position(turtles)
user_bet = screen.textinput(title="Make your bet", prompt="Enter the color of the turtle that will win the race:")

if user_bet:
    is_race_on = True

while is_race_on:
    turtle = choice(turtles)
    turtle[0].forward(10)
    if finish_line(turtle[0]):
        is_race_on = False
        winner = turtle[1]
        screen.textinput(title="Game Over", prompt="The winner is : " + winner)
        if winner == user_bet:
            screen.textinput(title="Game Over", prompt="You guessed the winner")
        else:
            screen.textinput(title="Game Over", prompt="You are not a good guesser.")

screen.exitonclick()

