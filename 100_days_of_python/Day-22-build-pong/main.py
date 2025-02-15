from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")

game_is_on = True
sleep = 0.1
while game_is_on:
    screen.update()
    time.sleep(sleep)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with r_paddle / l_paddle 
    
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        sleep *= 0.5
        


    #Detect when the r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.scored_l()
        sleep = 0.5

    #Detect when the l_paddle misses the ball 
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.score_r()
        sleep = 0.1



screen.exitonclick()
