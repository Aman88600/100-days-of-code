from turtle import Turtle, Screen
from random import randint

spot_pen = Turtle()
window = Screen()
spot_pen.speed(0)

width = 600
height = 600
window.setup(height, width)

spot_pen.penup()

def random_color():
    red = randint(0, 255) / 255
    green = randint(0, 255) / 255
    blue = randint(0, 255) / 255
    return (red, green, blue)

for y in range(-200, 201, 50):
    for x in range(-200, 201, 50):
        spot_pen.goto(x, y)
        spot_pen.dot(20, random_color())

window.exitonclick()