from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
from pyperclip import copy


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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
    password = ''.join(password_list)

    password_entry.insert(0, password)
    copy(password)
    generate_password_button.config(text='Reset', width=14)
    if len(password_entry.get()) > len(password):
        password_entry.delete(0, END)
        generate_password_button.config(text='Generate Password')



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    website_entry.delete(0, END)

    username = email_username_entry.get()

    password = password_entry.get()
    password_entry.delete(0, END)

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo('Oops', "Please don't leave any of the fields empty!")
        generate_password_button.config(text='Generate Password')
    else:
        is_ok = messagebox.askokcancel('Ok?', 'These are the details entered: \nEmail: {username}\nPassword: {password}')
        if is_ok:
            with open('data.txt', 'a') as f:
                f.writelines(f"{website} | {username} | {password}\n")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=20)
window.title('Password Manager')

# CANVAS
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky='ew', columnspan=2)
website_entry.focus()

email_username_entry = Entry()
email_username_entry.grid(column=1, row=2, sticky='ew', columnspan=2)
email_username_entry.insert(0, 'kadewilliams0@gmail.com')

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky='ew', columnspan=2)

# Buttons
generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='ew')

add_button = Button(text='Add', width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='ew')

window.mainloop()
