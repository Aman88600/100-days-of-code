from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    number_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    char_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = number_list + symbol_list + char_list

    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    password_entry.delete(0,END)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# save password funciton
def save_password():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="website or password section is empty")
    else:
        data = f"{website} | {email} | {password}\n"
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details you entered\nEmail : {email}\npassword : {password}\nIs It OK?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(data)

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# 1 Make a window (Done)
# 2 Set the title of the window to Password Manager(Done)
# 3 Make a canvas widget with logo.png image(Done)
# 4 Make the window padding 20(Done)
# 5 website label in row 1 column 0 (Done)
# 6 taking website input on row 1 column 1 (Done)
# 7 Email/Username Label (Done)
# 8 Email/Username Entry (Done)
# 9 Password label (Done)
# 10 Password Entry (Done)
# 11 generate password button (Done)
# 12 Add Button (Done)

# Window created
window = Tk()
# Setting the window title
window.title("Password Manager")
window.config(padx=20, pady=20)
# Making a canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = mypass_img) # The center of the image is at (100,100)
canvas.grid(row=0, column=1)

# website label
website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0, columnspan=1)
# website entry
website_entry = Entry(window, width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
# username label
username_label = Label(window, text="Email/Username:")
username_label.grid(row=2, column=0)
# username Entry
username_entry = Entry(window, width=50)
username_entry.insert(0, "amanbasoya02@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)
# Password Label
password_label = Label(window, text="Password")
password_label.grid(row=3, column=0)
# Password Entry
password_entry = Entry(window, width=32)
password_entry.grid(row=3, column=1, columnspan=1)
# Generate Password Button
generate_entry = Button(window, text="Generate Password", width=14, command=generate_password)
generate_entry.grid(row=3, column=2, columnspan=1)

# Add button
add_button = Button(window, text="Add", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
# Main loop set
window.mainloop()