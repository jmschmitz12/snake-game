from turtle import Turtle
import random


class Target:
    def __init__(self):
        self.target = Turtle("square")
        self.target.color("white")
        self.target.penup()
        self.x = None
        self.y = None


    def update(self):
        self.x = round(random.randint(-280, 280) / 20) * 20
        self.y = round(random.randint(-280, 280) / 20) * 20
        self.target.hideturtle()
        self.target.setposition(self.x, self.y)
        self.target.showturtle()
        print(f"Target position: {(self.x, self.y)}")
