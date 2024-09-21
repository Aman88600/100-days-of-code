from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
for i in range(10):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(180)
screen = Screen()
screen.exitonclick()