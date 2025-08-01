# Make Decorators to styles the HTML

from flask import Flask

app = Flask(__name__)

# 1 Bold b(Done)
# 2 Emphaise em (Done)
# 3 Underline u (Done)

def bold_decorator(function):
    def wrapper_funciton():
        string = function()
        # Modify that string to add bold tags
        new_string = "<b>" + string + "</b>"
        return new_string
    return wrapper_funciton

def emphasis_decorator(function):
    def wrapper_funciton():
        string = function()
        # Modify that string to add bold tags
        new_string = "<em>" + string + "</em>"
        return new_string
    return wrapper_funciton

def underline_decorator(function):
    def wrapper_funciton():
        string = function()
        # Modify that string to add bold tags
        new_string = "<u>" + string + "</u>"
        return new_string
    return wrapper_funciton

@app.route("/")
@bold_decorator
@emphasis_decorator
@underline_decorator
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)