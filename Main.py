from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title('Ping Pong')
screen.tracer(0)

right = Paddle((350, 0))
left = Paddle((-350, 0))

screen.listen()

screen.onkeypress(right.move_up, 'Up')
screen.onkeypress(right.move_down, 'Down')

screen.onkeypress(left.move_up, 'w')
screen.onkeypress(left.move_down, 's')

ball = Ball()

scoreboard = Scoreboard()

game_on = True
while game_on:
    time.sleep(ball.speeed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
        
    if ball.distance(right) < 50 and ball.xcor() > 320:
        ball.bouncex()
        
    if ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bouncex()
        
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.point_l()
        
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.point_r()










screen.exitonclick()