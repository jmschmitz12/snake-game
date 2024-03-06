from turtle import Turtle


class Segment:
    """segment of a snake"""
    def __init__(self, x, y):
        self.segment = Turtle("square")
        self.segment.hideturtle()
        self.segment.color("white")
        self.segment.penup()
        self.x = x
        self.y = y
        self.segment.setposition(self.x, self.y)
        self.segment.showturtle()

    def update(self):
        self.segment.setposition(self.x, self.y)
