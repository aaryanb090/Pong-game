# funny bounces when the ball collides at the edge of the paddle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_l.up, "Left")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeypress(paddle_l.down, "Right")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Detect paddle r misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.point_l()

    # Detect paddle l misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.point_r()

screen.exitonclick()
