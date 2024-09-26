from turtle import Screen, Turtle
from random import randint

window = Screen()
window.setup(width=500, height=500)
window.title("Turtle Race")

# This funciton makes the racing turtles
def make_turtle(turtle_name, turtle_color, turtle_position):
    turtle_name = Turtle()
    turtle_name.shape("turtle")
    turtle_name.color(f"{turtle_color}")
    turtle_name.penup()
    turtle_name.goto(-200, turtle_position)    
    return turtle_name

# Making the racing turtles
turtles = [
    make_turtle("purple_turtle", "purple", 200),
    make_turtle("blue_turtle", "blue", 150),
    make_turtle("green_turtle", "green", 100),
    make_turtle("yellow_turtle", "yellow", 50),
    make_turtle("orange_turtle", "orange", 0),
    make_turtle("red_turtle", "red", -50)
    ]
# Getting user choice
user_choice = window.textinput("Welcome to Turtle Race", "Choose Your Turtle : ")

keep_going = True
winner = turtles[0]
while keep_going:
    for turtle in turtles:
        current_position = turtle.pos()
        x_position = current_position[0]
        if x_position > 250:
            winner = turtle
            keep_going = False
        else:
            movement = randint(1,10)
            turtle.forward(movement)
window.bye()
if user_choice == winner.pencolor():
    print(f"You win!, The winner is {winner.pencolor()}")
else:
    print(f"You Lose!, The winner is {winner.pencolor()}")
