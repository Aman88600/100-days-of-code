from turtle import Turtle, Screen
from math import sqrt
from random import randint

drawing_pen = Turtle()
drawing_pen.speed(0)



steps = 8


def random_color():
    red = randint(0, 255) / 255
    green = randint(0, 255) / 255
    blue = randint(0, 255) / 255
    return (red, green, blue)
def draw_circle(x, y):
    drawing_pen.color(random_color())
    drawing_pen.penup()
    drawing_pen.goto(x,y)
    drawing_pen.pendown()
    drawing_pen.circle(100)    

x_pos = - 100
y_pos = 0
for x in range(-100, 101, steps):
    x_pos = x
    y_pos = sqrt(10000 - x_pos ** 2)
    draw_circle(x_pos, y_pos)


for x in range(100, -101, -steps):
    x_pos = x
    y_pos = -sqrt(10000 - x_pos ** 2)
    draw_circle(x_pos, y_pos)

window = Screen()
window.exitonclick()