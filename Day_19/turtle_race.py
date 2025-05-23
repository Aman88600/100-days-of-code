# Turtle Race
from turtle import Turtle, Screen, textinput
from random import randint

window = Screen()
# Setting window dimentions
window.setup(width=600, height=600)

user_input = textinput('Make your bet', 'Which turtle will win : ')
class make_turtle:
    def __init__(self, name, t_color, posx, posy):
        self.name = Turtle()
        self.name.shape('turtle')
        self.name.penup()
        self.name.color(t_color)
        self.name.goto(posx, posy)
        self.color = t_color

    def move(self):
        self.name.forward(randint(1,10))

    def get_pos(self):
        return self.name.position()[0]

turtles = {}
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'pink']
for i in range(0, 6):
    turtles[f"turtle_{i}"] = make_turtle("turtle_1", colors[i], -250, (window.window_height()/2) - 50 - (i * 100))

keep_going = True
while keep_going:
    for i in turtles:
        if turtles[i].get_pos() >= 250:
            print(f"Winner is {turtles[i].color}")
            if user_input == turtles[i].color:
                print("You win the bet")
            else:
                print("You lose the bet")
            keep_going = False
            break
    for i in turtles:
        turtles[i].move()

# turtle_1.get_pos()
window.exitonclick()