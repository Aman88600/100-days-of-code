from turtle import Turtle, Screen
from random import randint


different_shapes = Turtle()

def new_color():
    red = randint(0, 255) / 255
    green = randint(0, 255) / 255
    blue = randint(0, 255) / 255
    return (red, blue, green)

different_shapes.penup()
different_shapes.goto(100,100)
different_shapes.pendown()

for i in range(3, 11):
    different_shapes.color(new_color())
    for j in range(1, i + 1):
        angle = ((i - 2) * 180) / i
        angle = 180 - angle
        different_shapes.right(angle)
        different_shapes.forward(100)


window = Screen()
window.exitonclick()