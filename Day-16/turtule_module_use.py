# from turtle import Turtle, Screen
# # from another_module import another_variable
# # print(another_variable)

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")

# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.forward(100)

# # This function will hold the screen until we click in it
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)