from turtle import Turtle, Screen
# from another_module import another_variable
# print(another_variable)

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue", "blue")

my_screen = Screen()
print(my_screen.canvheight)

# This function will hold the screen until we click in it
my_screen.exitonclick()