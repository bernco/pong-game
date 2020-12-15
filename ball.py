from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.pu()
        self.x_move = 10
        self.y_move = 10
        self.speed_ball = 0.1

    def ball_movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball_y(self):
        self.y_move *= -1

    def bounce_ball_x(self):
        self.x_move *= -1
        self.speed_ball *= 0.8

    def game_reset(self):
        self.home()
        self.speed_ball = 0.1
        self.bounce_ball_x()

