from turtle import Screen, Turtle
from playerPaddle import PaddlePlayer
from ball import Ball
import time
from scoreboard import ScoreBoard

game_screen = Screen()
game_screen.bgcolor("black")
game_screen.setup(width=800, height=600)
game_screen.title("Bernco Pong Game")

game_screen.tracer(0)
divider = Turtle()
divider.hideturtle()
divider.color("white")
divider.pensize(width=3)
divider.pu()
divider.setpos(0, -280)

right_paddle = PaddlePlayer((350, 0))
left_paddle = PaddlePlayer((-350, 0))
game_ball = Ball()
my_scoreboard = ScoreBoard()
for _ in range(30):
    divider.pd()
    divider.seth(90)
    divider.forward(10)
    divider.pu()
    divider.forward(10)


game_screen.listen()
game_screen.onkeypress(key="Up", fun=right_paddle.move_up)
game_screen.onkeypress(key="Down", fun=right_paddle.move_down)
game_screen.onkeypress(key="q", fun=left_paddle.move_up)
game_screen.onkeypress(key="z", fun=left_paddle.move_down)


game_is_on = True
while game_is_on:
    time.sleep(game_ball.speed_ball)
    game_ball.ball_movement()

    # detects collision with the top and bottom boundaries
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_ball_y()

    # detects collision with the paddles
    if game_ball.xcor() > 320 and game_ball.distance(right_paddle) < 50 or game_ball.xcor() < -320 \
            and game_ball.distance(left_paddle) < 50:
        game_ball.bounce_ball_x()

    # detects out of right players bound
    if game_ball.xcor() > 400:
        game_ball.game_reset()
        my_scoreboard.add_left_score()

    # detects out of left players bound
    if game_ball.xcor() < -400:
        game_ball.game_reset()
        my_scoreboard.add_right_score()

    game_screen.update()

game_screen.exitonclick()
