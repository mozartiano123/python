from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONTCOLOR = "Black"



class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(FONTCOLOR)
        self.goto(-280, 260)
        self.level = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", move=False, align="left", font=FONT)

    def increase_score(self, player):
        if player == 1:
            self.score_p1 += 1
        elif player == 2:
            self.score_p2 += 1

        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=FONT)


