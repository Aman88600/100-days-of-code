from flask import Flask, render_template, request, redirect, url_for
import sqlite3


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    # Connect to the database
    db = sqlite3.connect('books-collection.db')
    cursor = db.cursor()
    # Checking If there no book
    cursor.execute("SELECT * FROM books_table")
    rows = cursor.fetchall()
    db.close()
    if len(rows) == 0:
        no_books = True
    else:
        no_books = False
    return render_template("index.html", books=rows, no_books=no_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = request.form.get('book_name', None)
        author = request.form.get('author_name', None)
        rating = str(request.form.get('rating', None))
        # Temperorary Memory
        all_books.append({'book':book, 'author' : author, 'rating':rating})
        # Permanent memory
        #Making an entry
        db = sqlite3.connect('books-collection.db')
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO books_table (book_name, author_name, rating) VALUES (?, ?, ?)",
            (book, author, rating)
        )
        db.commit()
        db.close()
        return redirect('/')
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

