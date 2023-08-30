from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = []
    password_symbols = []
    password_numbers = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(END, 0)
    password_entry.insert(END, password)
    # print(f"Your password is: {password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info():
    website_text = website_entry.get()
    email_text = email_username_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_text: {
            "email": email_text,
            "password": password_text
        }
    }
    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave fields empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old Data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------------FIND PASSWORD---------------------------------#

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file Found!")
    else:

        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=60, padx=60)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", fg='black')
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", fg="black")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password", fg="black")
password_label.grid(column=0, row=3)

website_entry = Entry(width=23)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

email_username_entry = Entry(width=40)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(END, "pavaniv29@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", fg="black", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(width=34, text="Add")
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(command=save_info)

window.mainloop()
