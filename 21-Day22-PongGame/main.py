from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreBoard import Scoreboard
import time


#screen ops
window = Screen()
window.bgcolor("black")
window.setup(width=800, height=600)
window.title("Pong Game")
window.tracer(0)

# paddle class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Ball
ball = Ball()
# score
score = Scoreboard()



window.listen()
window.onkey(r_paddle.go_up, "Up")
window.onkey(r_paddle.go_down, "Down")
window.onkey(l_paddle.go_up, "w")
window.onkey(l_paddle.go_down, "s")


is_game_end = True
while is_game_end:
    time.sleep(ball.ball_speed)
    window.update()
    ball.move()

    # ball detection to wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

window.exitonclick()