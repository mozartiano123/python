from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier"
FONTSIZE = 12
FONTTYPE = "normal"
FONTCOLOR = "Yellow"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color(FONTCOLOR)
        self.goto(0, 280)
        self.score = -1
        self.high_score = 0
        self.load_highest_score()
        self.hideturtle()
        self.increase_score()


    def load_highest_score(self):
        with open("scores.txt") as file:
            self.high_score = int(file.read())


    def save_highest_score(self):
        with open("scores.txt", mode="w") as file:
                file.write(str(self.high_score))

    def update_scoreboard(self):
         self.clear()
         self.write(f"Player Score: {str(self.score)} High Score: {str(self.high_score)} " ,
                    move=False, align=ALIGNMENT, font=(FONT, FONTSIZE, FONTTYPE))
         self.save_highest_score()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

