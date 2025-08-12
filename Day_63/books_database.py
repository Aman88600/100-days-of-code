import sqlite3

# Connect to the database
db = sqlite3.connect('books-collection.db')
cursor = db.cursor()

# Execute query to check if any rows exist
cursor.execute("SELECT * FROM books_table")
rows = cursor.fetchall()

print(rows)
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS books_table (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         book_name TEXT NOT NULL,
#         author_name TEXT NOT NULL,
#         rating TEXT NOT NULL
#     )
# ''')

# db.commit()




# Making an entry
# cursor.execute(
#     "INSERT INTO books_table (book_name, author_name, rating) VALUES (?, ?, ?)",
#     ("The Alchemist", "Paulo Coelho", "4.5")
# )
# db.commit()

# Close the connection
db.close()