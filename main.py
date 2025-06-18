import random
import time
from turtle import Turtle, Screen
from score_board import Scoreboard

score = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.title("PONG!!!")
screen.setup(width=1000, height=800)
screen.tracer(0)

middle_border = Turtle()
game_over = Turtle()
game_over.hideturtle()
middle_border.color("white")
middle_border.shape("square")
middle_border.shapesize(stretch_wid=40, stretch_len=0.3)

ball = Turtle()
ball.penup()
right_bar = Turtle()
right_bar.penup()
ball.color("lime green")
ball_spawn_location = [(0, 0), (0, 100), (0, 200), (0, 280), (0, -100), (0, -200), (0, -280), (0, 150),
                       (0, -150),
                       (0, 50), (0, -50)]

ball.shape("circle")
random_ball_spawn_location = random.choice(ball_spawn_location)
ball.goto(random_ball_spawn_location)
right_bar.goto(480, 0)
right_bar.color("white")
right_bar.shape("square")
right_bar.shapesize(stretch_len=1, stretch_wid=5)


heading = 45
ycor = 0
def move_right():
   global ycor
   ycor += 77
   right_bar.goto(480, ycor)
def move_left():
   global ycor
   ycor -= 77
   right_bar.goto(480, ycor)

def bounce(x, y):
   global heading
   if float(ball.xcor()) > x:
      if heading == 45:
         heading = 135
      elif heading == 315:
         heading = 225
   if float(ball.xcor()) < -x:
      if heading == 135:
         heading = 45
      elif heading == 225:
         heading = 315
   if float(ball.ycor()) > y:
      if heading == 135:
         heading = 225
      elif heading == 45:
         heading = 315
   if float(ball.ycor()) < -y:
      if heading == 315:
         heading = 45
      elif heading == 225:
         heading = 135
timesleep = 0.01
current_score = 0
game_is_on = True
while game_is_on:
   screen.update()
   time.sleep(timesleep)
   ball.setheading(heading)
   ball.forward(5)
   bounce(480, 380)
   if ball.distance(right_bar) < 60:
      bounce(451.548339959392, 380)
   if ball.xcor() >= 480:
      game_is_on = False
      game_over.color("lime green")
      game_over.write("GAME OVER", align="center", font=("courier", 25, "normal"))
   if ball.xcor() == 452.548339959392:
      current_score += 1
      print(ball.xcor())
   score.num_one(current_score)



   screen.listen()
   screen.onkey(move_right, "Up")
   screen.onkey(move_left, "Down")


screen.exitonclick()