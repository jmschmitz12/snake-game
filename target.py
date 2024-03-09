from turtle import Turtle
import random


class Target(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = None
        self.y = None


    def update(self):
        self.x = round(random.randint(-280, 280) / 20) * 20
        self.y = round(random.randint(-280, 280) / 20) * 20
        self.hideturtle()
        self.setposition(self.x, self.y)
        self.showturtle()
        print(f"Target position: {(self.x, self.y)}")
