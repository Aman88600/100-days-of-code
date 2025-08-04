from flask import Flask, render_template
from random import randint
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    random_number = randint(1,10)
    current_year = datetime.now()
    current_year = str(current_year).split('-')[0]
    return render_template("index.html", num=random_number, year=current_year)
if __name__ == "__main__":
    app.run(debug=True)