from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")
SCORE_POSITION_LEFT = -100, 230
SCORE_POSITION_RIGHT = 100, 230


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.setpos(SCORE_POSITION_LEFT)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.setpos(SCORE_POSITION_RIGHT)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)

    def add_left_score(self):
        self.left_score += 1
        self.refresh_score()

    def add_right_score(self):
        self.right_score += 1
        self.refresh_score()
