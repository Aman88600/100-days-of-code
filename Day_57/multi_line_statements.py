from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def index():
    random_number = randint(1,10)
    current_year = datetime.now()
    current_year = str(current_year).split('-')[0]
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/blog")
def blog():
    blog_posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog_posts = eval(blog_posts.text)
    return render_template("blog.html", blog_posts=blog_posts)

# Runninf the app
if __name__ == "__main__":
    app.run(debug=True)