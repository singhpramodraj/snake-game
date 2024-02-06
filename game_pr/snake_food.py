from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
# here rather than creating the turtle as the attribute and then using it we have directly inherited the Turtle class
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.set_new()
        self.speed("fastest")


    def set_new(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setpos(random_x, random_y)