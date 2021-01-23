from turtle import Turtle

class Map(Turtle):

    def __init__(self, x, y, state_name):
        super().__init__()
        self.state_name = state_name
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.write(f"{str(self.state_name)}", move=False, align="center", font=("Courier", "8", "normal"))