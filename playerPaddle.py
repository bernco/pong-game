from turtle import Turtle


# PaddlePlayer class inherits from the Turtle class
class PaddlePlayer(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.pu()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setpos(position)

    # moves the paddle up
    def move_up(self):
        x_pos = self.xcor()
        y_pos = self.ycor() + 20
        self.goto(x_pos, y_pos)

    # moves the paddle down
    def move_down(self):
        x_pos = self.xcor()
        y_pos = self.ycor() - 20
        self.goto(x_pos, y_pos)
