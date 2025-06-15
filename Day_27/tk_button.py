from tkinter import *

window = Tk()

#Label
new_label = Label(text="0")
new_label.pack()


# Entry
input = Entry(width=10)
input.pack()


# Button
def button_click():
    # num = int(new_label["text"])
    # num += 1
    new_label["text"] = input.get()
my_button = Button(text="This is a button", command=button_click)
my_button.pack()


window.mainloop()