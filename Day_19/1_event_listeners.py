from turtle import Turtle, Screen

tim = Turtle()
window = Screen()

def move_forward():
    tim.forward(10)
window.listen()
window.onkey(key="space", fun=move_forward)
window.exitonclick()