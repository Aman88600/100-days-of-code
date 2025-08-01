from flask import Flask
from random import randint

app = Flask(__name__)

# Generating a random number
random_number = randint(0,9)

# Website front page
@app.route("/")
def higher_lower_front():
    return """<h1>Guess a number between 0 and 9</h1>\n
            <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>
            """

# Actual plating route and function
@app.route("/<int:guess>")
def guess_function(guess):
    if guess > random_number:
        return '''<h1 style="color:purple;">Too high, try again!</h1>
                    <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'''
        
    elif guess < random_number:
        return '''<h1 style="color:red;">Too Low, try again!</h1>
                    <img src = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'''
    elif guess == random_number:
        return '''<h1 style="color:green;">You found me!</h1>
                    <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'''


if __name__ == "__main__":
    app.run(debug=True)