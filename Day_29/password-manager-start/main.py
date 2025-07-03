from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# save password funciton
def save_password():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    data = f"{website} | {email} | {password}\n"

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
generate_entry = Button(window, text="Generate Password", width=14)
generate_entry.grid(row=3, column=2, columnspan=1)


# Add button
add_button = Button(window, text="Add", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
# Main loop set
window.mainloop()