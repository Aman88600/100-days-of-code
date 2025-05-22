import turtle
from random import randint

turtle.colormode(255)
window = turtle.Screen()
window.setup(width=500, height=500)
timmy = turtle.Turtle()
timmy.penup()

# Generate random colors
def get_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)
timmy.speed(0)
timmy.goto(-200,200)
while timmy.position()[1] >= -200: 
    while timmy.position()[0] <= 200:
        timmy.dot(10, get_color())
        timmy.forward(50)
    timmy.goto(-200,timmy.position()[1] - 50)


window.exitonclick()