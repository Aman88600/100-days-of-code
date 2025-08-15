from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB


# CREATE TABLE


@app.route("/", methods=['GET', 'POST'])
def home():
    #Making or conneting to the database
    db = sqlite3.connect('top_10_movies.db')
    # Making a cursor
    cursor = db.cursor()
    # Execute query to check if any rows exist
    cursor.execute("SELECT * FROM movies_table")
    rows = cursor.fetchall()
    db.close()

    # Sort the list by the score (5th element) in descending order
    sorted_movies_desc = sorted(rows, key=lambda x: int(x[4]), reverse=True)

    # Add the rank to each movie based on the sorted order
    ranked_movies_desc = [(movie[0], movie[1], movie[2], movie[3], movie[4], movie[5], movie[6], movie[7], idx+1) for idx, movie in enumerate(sorted_movies_desc)]

    # Checkinf if we have reached 10 movies
    add_movies = True
    if len(rows) == 10:
        add_movies = False
    return render_template("index.html", rows=ranked_movies_desc[::-1], add_movies = add_movies)


@app.route("/delete/<title>", methods=["GET", "POST"])
def delete(title):
    if request.method == "GET":
        try:
            # Using context manager to handle connection and ensure closure
            with sqlite3.connect('top_10_movies.db', timeout=10) as db:
                cursor = db.cursor()
                # Delete the movie based on the title
                cursor.execute(
                    "DELETE FROM movies_table WHERE title = ?",
                    (title,)  # Ensure this is a tuple
                )
                db.commit()

            return redirect(url_for('home'))  # Redirect to the home page after deletion
        except sqlite3.OperationalError as e:
            # Handle potential database issues, such as being locked
            print(f"Database error: {e}")
            return "Database is currently locked or another error occurred. Please try again later."


@app.route("/update/<title>", methods=["GET", "POST"])
def update(title):
    if request.method == "POST":
        print(title)
        rating = str(request.form.get('rating'))
        review = str(request.form.get('review'))
        #Making or conneting to the database
        db = sqlite3.connect('top_10_movies.db')
        # Making a cursor
        cursor = db.cursor()
        # Update the movie in the database
        cursor.execute(
            "UPDATE movies_table SET rating = ?, review = ? WHERE title = ?",
            (rating, review, title)
        )
        db.commit()
        db.close()
        return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template("edit.html", movie_title=title)
    
@app.route('/add/', methods=["GET", "POST"])
def add_movie():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        title = request.form["title"]
        year = request.form["year"]
        description = request.form["description"]
        rating = request.form["rating"]
        review = request.form["review"]
        img_url = request.form["img_url"]

        print(title, year, description, rating, review, img_url)
        
        # Using context manager to automatically handle connection closing
        with sqlite3.connect('top_10_movies.db') as db:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO movies_table (title, year, description, rating, ranking, review, img_url) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (title, year, description, rating, 1, review, img_url)
            )
            db.commit()

        return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
