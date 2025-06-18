from turtle import Turtle
import random

class Scoreboard:
    def __init__(self):
        self.one = Turtle()
        # self.two = Turtle()
        # self.three = Turtle()
        # self.four = Turtle()
        # self.five = Turtle()
        # self.six = Turtle()
        # self.seven = Turtle()
        # self.eight = Turtle()
        # self.nine = Turtle()


    def num_one(self, inpu):
        self.one.color("white")
        self.one.penup()
        self.one.hideturtle()
        self.one.goto(x=-270, y=200)
        self.one.clear()
        self.one.write(f"{inpu}", font=("courier", 75, "normal"))