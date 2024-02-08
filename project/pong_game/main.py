import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# paddle = Paddle()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
speed = 0.1
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 60 and ball.xcor() > 340) or (ball.distance(l_paddle) < 60 and ball.xcor() < - 340):
        ball.bounce_x()
        speed -= 1

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()





#Todo 1: Create a screen
#Todo 2: create and move paddle
#Todo 3: Move another paddle
#Todo 4: create the ball and move
#Todo 5: Collision with wall and move
#Todo 6: Detect collision with paddle
#Todo 7: Detect when paddle missies ball
#Todo 8: Score