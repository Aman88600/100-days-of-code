from turtle import Turtle, Screen
from random import randint

random_walk = Turtle()
window = Screen()
height = window.window_height() / 2
width = window.window_width() / 2
random_walk.pensize(10)
random_walk.speed(0)


def random_color():
    red = randint(0, 255) / 255
    green = randint(0, 255) / 255
    blue = randint(0, 255) / 255
    return (red, green, blue)

def random_direction():
    direction = randint(1, 4)
    if direction == 1:
        return 90
    elif direction == 2:
        return 180
    elif direction == 3:
        return -90
    else:
        return 0 

for i in range(100):
    random_walk.color(random_color())
    random_walk.forward(40)
    random_walk.right(random_direction())
window.exitonclick()