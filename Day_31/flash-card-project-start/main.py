from tkinter import *
import csv
from random import randint
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Flipping card 



# Making a canvas
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file = "images/card_back.png")
def make_canvas(englis, french):
    def flip_card():
        canvas.itemconfig(card_front, image=card_back_img)
        canvas.itemconfig(language_text, text="English", fill="white")
        canvas.itemconfig(word_text, text=englis, fill="white")
    canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    card_front = canvas.create_image(400,263, image=card_front_img)
    language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
    word_text = canvas.create_text(400, 263, text=french, fill="black", font=("Arial", 60, "bold"))
    canvas.grid(row=0, column=0, columnspan=2)
    window.after(3000, flip_card)

words = []
with open("data/french_words.csv", "r") as csv_file:
    data = csv.reader(csv_file)
    for row in data:
        words.append(row)

# Known
known_words = []
# select a random word
word_num = randint(0, len(words) - 1)
while word_num in known_words:
    word_num = randint(0, len(words) - 1)
make_canvas(englis=words[word_num][1], french=words[word_num][0])


def cross_function():
    global known_words
    # known_words.append(word_num)
    # select a random word
    word_num = randint(0, len(words) - 1)
    while word_num in known_words:
        word_num = randint(0, len(words) - 1)
    make_canvas(englis=words[word_num][1], french=words[word_num][0])

def tick_function():
    global known_words
    global word_num
    known_words.append(word_num)
    # select a random word
    word_num = randint(0, len(words) - 1)
    while word_num in known_words:
        word_num = randint(0, len(words) - 1)
    make_canvas(englis=words[word_num][1], french=words[word_num][0])
    
# Cross BUtton
cross_image = PhotoImage(file = "images/wrong.png")
cross_button = Button(window, image=cross_image, highlightthickness=0, command=cross_function)
cross_button.grid(row=1, column=0)
# Tick Button
tick_image = PhotoImage(file = "images/right.png")
tick_button = Button(window, image=tick_image, highlightthickness=0, command=tick_function)
tick_button.grid(row=1, column=1)
window.mainloop()