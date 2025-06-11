import turtle
import pandas
window = turtle.Screen()

# Turtle only supports .gif format
us_image = "blank_states_img.gif"
# Here we areadding a new type of image
window.addshape(us_image)
# Here we add a turtle with the shape of image we described
turtle.shape(us_image)
window.title("U.S. States Game!")




# Writing text on a specific position
def write_text(text_to_write, x, y):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(x,y)
    text.write(text_to_write, font=("Arial", 7, "normal"))


# Getting CSV data
data = pandas.read_csv("50_states.csv")
states = list(data["state"])
guessed_states = []

while len(guessed_states) <= 49:
    # Getting User Input
    answer = window.textinput(title=f" {len(guessed_states)}/50 Guess the State", prompt="What's another state")

    # Checking
    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
    print(guessed_states)
    # Matching the user input with csv data
    df = data[data.state == answer]
    if len(df) != 0:
        # Writing the correct state on the map
        write_text(answer, list(df.x)[0], list(df.y)[0])
    else:
        print("Not a State")

window.exitonclick()