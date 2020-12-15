from turtle import Turtle


# our Ball class inherits from the Turtle class
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.pu()
        self.x_move = 10
        self.y_move = 10
        self.speed_ball = 0.1

    # moves the ball
    def ball_movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # bounces the ball when touch the two vertical walls
    def bounce_ball_y(self):
        self.y_move *= -1

    # bounces the ball when touch the two paddles
    def bounce_ball_x(self):
        self.x_move *= -1
        self.speed_ball *= 0.8

    # resets the game by moving the ball and the speed to their initial position
    def game_reset(self):
        self.home()
        self.speed_ball = 0.1
        self.bounce_ball_x()

