from turtle import Turtle
WIDTH = 1
HEIGHT = 5
UP = 20
DOWN = -20

class Paddle(Turtle):

    def __init__(self, x_cor: object, y_cor: object) -> object:
        self.x = x_cor
        self.y = y_cor
        super().__init__("square")
        self._tracer(0)
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.new_position(self.x, self.y, 0)

    def new_position(self, x_cor, y_cor, direction):
        new_x = x_cor
        new_y = y_cor + direction
        self.goto(x=new_x, y=new_y)


    def go_up(self):
        self.new_position(self.xcor(), self.ycor(), UP)


    def go_down(self):
        self.new_position(self.xcor(), self.ycor(), DOWN)
