# Guessing the age and gender using name
from flask import Flask, render_template
import requests
app = Flask(__name__)


def get_gender(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    return ((eval(response.text))['gender'])

def get_age(name):
    response = requests.get(f"https://api.agify.io/?name={name}")
    return ((eval(response.text))['age'])


@app.route("/guess/<name>")
def index(name):
    gender = get_gender(name)
    age = get_age(name)
    return render_template("index.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)