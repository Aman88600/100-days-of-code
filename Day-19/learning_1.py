from turtle import Turtle, Screen

tim = Turtle()
window = Screen()

def move_forward():
    tim.forward(10)

def hello():
    print("Hello, World!")

window.listen()
window.onkey(key="space", fun=move_forward) # onkey is a higher order function, reason is because it can take other function as input
window.onkey(key="w", fun=hello)
window.exitonclick()