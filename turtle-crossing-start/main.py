import time
from turtle import Screen
from player import Player
from car_manager import CarManager
import random
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

speed = 0.1

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    #check collision with cars.
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            screen.update()

    #check finish line.
    if player.cross_finish_line():
        scoreboard.update_scoreboard()
        car_manager.level_up()




screen.exitonclick()