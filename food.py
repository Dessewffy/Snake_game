from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

# Randomisation of the "food"
    def refresh(self):
        randomX = random.randint(-200, 200)
        randomY = random.randint(-200, 200)
        self.goto(randomX, randomY)
