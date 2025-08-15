import sqlite3

#Making or conneting to the database
db = sqlite3.connect('top_10_movies.db')
# Making a cursor
cursor = db.cursor()

# # Making the table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS movies_table (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT UNIQUE NOT NULL,
#         year TEXT NOT NULL,
#         description TEXT NOT NULL,
#         rating TEXT NOT NULL,
#         ranking INT NOT NULL,
#         review TEXT NOT NULL,
#         img_url TEXT NOT NULL
#     )
# ''')
# # Commiting the table
# db.commit()

# Execute query to check if any rows exist
cursor.execute("SELECT * FROM movies_table")
rows = cursor.fetchall()
print(rows)



# cursor.execute(
#     "INSERT INTO movies_table (title, year, description, rating, ranking, review, img_url) VALUES (?, ?, ?, ?, ?, ?, ?)",
#     ("Drive", "2011", "Loved it!", "7.5", 1, "A mysterious Hollywood stuntman and mechanic moonlights as a getaway driver and finds himself in trouble when he helps out his neighbor in this action drama.", "https://target.scene7.com/is/image/Target/GUEST_e4fa5671-3857-46ef-8529-78b011b758f8?wid=1200&hei=1200&qlt=80&fmt=webp")
# )
# db.commit()

# cursor.execute("UPDATE movies_table SET rating = '10', review = 'Hell' WHERE title = 'Drive'")
# db.commit()

# Closing the database connection
db.close()
