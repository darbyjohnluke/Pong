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
game_over = Turtle()
game_over.hideturtle()

def border():
   middle_border = Turtle()
   middle_border.color("white")
   middle_border.shape("square")
   middle_border.shapesize(stretch_wid=100, stretch_len=0.01)
   middle_border.penup()
   return middle_border

right_border = border()
right_border.goto(490, 0)
left_border = border()
left_border.goto(-497, 0)
upper_border = border()
upper_border.goto(0, 397)
upper_border.setheading(270)
lower_border = border()
lower_border.goto(0, -390)
lower_border.setheading(270)
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


heading = 33
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
      if 0 <= heading <= 90:
         heading = 180 - heading
      elif 270 < heading < 360:
         heading = 540 - heading
   if float(ball.xcor()) < -x:
      if 90 < heading <= 180:
         heading = 180 - heading
      elif 180 < heading < 270:
         heading = 540 - heading
   if float(ball.ycor()) > y:
      if 0 <= heading <= 180:
         heading = 360 - heading
   if float(ball.ycor()) < -y:
      if 270 < heading < 360 or 180 < heading <= 270:
         heading = 360 - heading

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
      if 450 < ball.xcor() < 455:
         current_score += 1
         timesleep = timesleep/1.3
         print(ball.xcor())
   score.num_one(current_score)

   if ball.xcor() >= 480:
      game_is_on = False
      game_over.color("lime green")
      game_over.write("GAME OVER", align="center", font=("courier", 25, "normal"))
   # if 450 < ball.xcor() < 455:
   #    current_score += 1

   # score.num_one(current_score)



   screen.listen()
   screen.onkey(move_right, "Up")
   screen.onkey(move_left, "Down")


screen.exitonclick()
