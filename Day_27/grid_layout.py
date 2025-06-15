from tkinter import *

window = Tk()

# Grid
# Label 0,0
first_label = Label(text="First Label 0 0")
first_label.grid(row=0, column = 0)

# Button 1 1
first_button = Button(text="First Button 0 0")
first_button.grid(row=1, column=1)

# Button 0 2
second_button = Button(text="Button 0 2")
second_button.grid(row=0, column=2)

# Entry 2 3
first_entry = Entry()
first_entry.grid(row=2, column=3)
window.mainloop()