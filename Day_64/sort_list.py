# List of tuples with movie information
movies = [
    (1, 'Drive', '2011', 'Loved it!', '6', 1, 'This was above average', 'https://target.scene7.com/is/image/Target/GUEST_e4fa5671-3857-46ef-8529-78b011b758f8?wid=1200&hei=1200&qlt=80&fmt=webp'),
    (2, 'Silence Of the lambs', '1991', 'Hannibal Lector', '10', 1, 'Bone Chilling!', 'https://imgs.search.brave.com/2L8Hnrki_78NMURbP5HXY_Z_j6e09-t5bl7sg5kdEGY/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL00v/TVY1QllUTXpZMlV5/WldVdE5qVXhNeTAw/WldSbUxXSmxZV1l0/TURVMU1HRXlZVEky/TVdRNFhrRXlYa0Zx/Y0djQC5qcGc'),
    (3, 'Inception', '2010', 'Mind-bending thriller', '8', 1, 'Great visuals and plot', 'https://example.com/inception.jpg'),
    (4, 'The Matrix', '1999', 'Reality-bending sci-fi', '9', 1, 'A classic!', 'https://example.com/matrix.jpg'),
    (5, 'The Godfather', '1972', 'Iconic crime drama', '7', 1, 'Masterpiece of cinema', 'https://example.com/godfather.jpg')
]

# Sort the list by the score (5th element) in descending order
sorted_movies_desc = sorted(movies, key=lambda x: int(x[4]), reverse=True)

# Add the rank to each movie based on the sorted order
ranked_movies_desc = [(movie[0], movie[1], movie[2], movie[3], movie[4], movie[5], movie[6], movie[7], idx+1) for idx, movie in enumerate(sorted_movies_desc)]

# Display the ranked list
for movie in ranked_movies_desc:
    print(movie)
