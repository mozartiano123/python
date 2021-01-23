from turtle import Turtle
WIDTH = 1
HEIGHT = 1
UP = 20
DOWN = -20
TOP = 280
BOTTOM = -280
DISTANCE = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self._tracer(0)
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.x_move = DISTANCE
        self.y_move = DISTANCE
        self.move_speed = 1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed += 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed += 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 1
        self.bounce_x()