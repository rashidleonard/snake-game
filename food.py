from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")
        self.food_location()

    def food_location(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)


# Ok so im trying to see if my GiHub is properly linked to my pycharm. this is not part of the code
