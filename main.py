from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(bg="white")
window.config(pady=50, padx=50)

# Canvas

canvas = Canvas(width=200, height=200, background="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
# Website Label
website_label = Label(text="Website:")
website_label.config(bg="white", fg="black")
website_label.grid(row=1, column=0)
# User Label
user_label = Label(text="Email/Username:")
user_label.config(bg="white", fg="black")
user_label.grid(row=2, column=0)
# Password Label
password_label = Label(text="Password:")
password_label.config(bg="white", fg="black")
password_label.grid(row=3, column=0)

# Textbox
# Website entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.config(bg="white", fg="black", highlightthickness=0)
# User Entry
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.config(bg="white", fg="black", highlightthickness=0)
# Password Entry
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)
password_entry.config(bg="white", fg="black", highlightthickness=0)

# Buttons
# Generate Password button
pass_generator_button = Button(text="Generate Password")
pass_generator_button.config(bg="white", fg="black", highlightthickness=0, width=9)
pass_generator_button.grid(row=3, column=2)
# Add button
add_button = Button(text="Add")
add_button.config(bg="white", fg="black", width=32)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
