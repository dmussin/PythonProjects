from turtle import Screen
from paddles import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
#Tracer - turn off the animation
screen.tracer(0)


ball = Ball()
score = Score()



l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    ball.ball_move()
    time.sleep(ball.ball_speed)
    screen.update()


    #Detecting collition with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detecting collision with padles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detecting score
    if ball.xcor() > 370:
        ball.reset_position()
        score.increase_score_l()

    if ball.xcor() < -370:
        ball.reset_position()
        score.increase_score_r()


screen.exitonclick()