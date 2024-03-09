from turtle import Turtle


class Segment(Turtle):
    """segment of a snake"""
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.x = x
        self.y = y
        self.setposition(self.x, self.y)
        self.showturtle()

    def update(self):
        self.setposition(self.x, self.y)
