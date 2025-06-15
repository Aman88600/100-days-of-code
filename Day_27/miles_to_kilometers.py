from tkinter import *

window = Tk()
# Taking miles
miles_label = Label(text="Miles")
miles_label.grid(row=0, column = 0)
miles = Entry()
miles.grid(row=0, column=1)



# Kilometes Label
kilometers_label = Label(text="Kilometers")
kilometers_label.grid(row=1, column=0)
kilometers_number = Label(text="0")
kilometers_number.grid(row=1, column=1)



# Convert Button
def button_click():
    kilometers_number['text'] = float(miles.get()) * 1.609344
convert_button = Button(text="convert", command=button_click)
convert_button.grid(row=2, column=0)

window.mainloop()