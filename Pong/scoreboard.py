from turtle import Turtle

FONT = "Courier"
FONTSIZE = 16
FONTTYPE = "normal"
FONTCOLOR = "White"
ALIGNMENT = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(FONTCOLOR)
        self.goto(0, 280)
        self.score_p1 = 0
        self.score_p2 = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f" PlayerA {self.score_p1}  :  {self.score_p2} PlayerB",
                   move=False, align=ALIGNMENT, font=(FONT, FONTSIZE, FONTTYPE))

    def increase_score(self, player):
        if player == 1:
            self.score_p1 += 1
        elif player == 2:
            self.score_p2 += 1

        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=(FONT, FONTSIZE, FONTTYPE))

