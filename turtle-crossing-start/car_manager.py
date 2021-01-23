from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
HEIGHT = 1
WIDTH = 2

class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_y = random.randint(-250,250)
        random_change = random.randint(1,6)
        if random_change == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT





