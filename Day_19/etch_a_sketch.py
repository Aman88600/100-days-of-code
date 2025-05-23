# importing turtle and screen to use them
from turtle import Screen, Turtle

# Making a Turtle object
tim = Turtle()
window = Screen()
window.listen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def clockwise():
    tim.right(30)
def counter_clockwise():
    tim.left(30)
window.onkey(key="w", fun=move_forward) # Key word arguments are being used here
window.onkey(key="s", fun=move_backward) 
window.onkey(key="d", fun=clockwise)
window.onkey(key="a", fun=counter_clockwise)
window.exitonclick()