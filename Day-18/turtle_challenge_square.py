from turtle import Turtle, Screen

# Making a Turtle class object
square_turtle = Turtle()
# Changing the shape to square
square_turtle.shape("square")
# Making the turtle draw a square
for i in range(4):
    square_turtle.forward(100)
    square_turtle.right(90)


# Making the window hold until, the screen is clicked on or the cross button
window = Screen()
window.exitonclick()