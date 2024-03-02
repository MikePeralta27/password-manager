from tkinter import *
from tkinter import messagebox as mb, messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, password)
    pyperclip.copy(password)
    print(pyperclip.paste())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()

    if website == '' or email == '' or password == '':
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = mb.askokcancel(title=website, message=f' There are the details entered: \nEmail: {email}'
                                                      f'\nPassword: {password} \nIs it okay to save?')
        if is_ok:
            with open('password.txt', mode="a") as password_data:
                password_data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

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
website_entry.config(bg="white", fg="black")
website_entry.focus()
# User Entry
user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.config(bg="white", fg="black", highlightthickness=0)
user_entry.insert(END, "peralta.michael27@gmail.com")
# Password Entry
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)
password_entry.config(bg="white", fg="black", highlightthickness=0)

# Buttons
# Generate Password button
pass_generator_button = Button(text="Generate Password", command=generate_password)
pass_generator_button.config(bg="white", fg="black", highlightthickness=0, width=9)
pass_generator_button.grid(row=3, column=2)
# Add button
add_button = Button(text="Add", command=save_password)
add_button.config(bg="white", fg="black", width=32)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
