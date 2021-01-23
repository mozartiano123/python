from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("Black")
        self.penup()
        self.setheading(90)
        self._tracer(0)
        self.go_to_start()


    def move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def cross_finish_line(self):
        if self.ycor() > 280:
            self.go_to_start()
            return True
        return False




