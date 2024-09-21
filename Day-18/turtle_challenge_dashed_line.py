from turtle import Turtle, Screen

dashed_turtle = Turtle()
for i in range(50):
    if dashed_turtle.isdown():
        dashed_turtle.penup()
    else:
        dashed_turtle.pendown()
    dashed_turtle.forward(5)

window = Screen()
window.exitonclick()
