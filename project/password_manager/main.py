from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

GREEN = "#9fc5e8"
BLACK = "#000000"
FONT = "Courier"
GREY = "#7db2bc"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def gen_pass():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def update_details():
    website_name = website_entry.get()
    user_name = user_name_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email": user_name,
            "password": password,
        }
    }

    if len(website_name) == 0 or len(user_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please check the fields are filled correct")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- Find details ------------------------------- #
def search_details():
    website_name = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            if website_name in data:
                email = data[website_name]["email"]
                password = data[website_name]["password"]
            messagebox.showwarning(title="Search result", message=f"Email: {email} \nPassword: {password}")
    except FileNotFoundError:
        messagebox.showwarning(title="Search result", message=f"No file matching the search")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_manager_log = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_manager_log)
canvas.grid(row=0, column=1)

## Labels
website_label = Label(text="Website:", fg=GREEN, font=("Helvetica", 16, "bold"))
website_label.grid(row=1, column=0)
website_label.focus()

email_username_label = Label(text="Email/Username:", fg=GREEN, font=("Helvetica", 16, "bold"))
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:", fg=GREEN, font=("Helvetica", 16, "bold"))
password_label.grid(row=3, column=0)

## Entries
website_entry = Entry(width=22, highlightthickness=0)
website_entry.grid(row=1, column=1)

user_name_entry = Entry(width=35, highlightthickness=0)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, "dhruv@gmail.com")

password_entry = Entry(width=22, highlightthickness=0)
password_entry.grid(row=3, column=1)

gen_pass_button = Button(text="Generate Password", bg=GREY, fg=GREEN, width=12, font=("Helvetica", 10, "bold"), highlightthickness=0, command=gen_pass)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=41, bg=GREY, fg=GREEN, font=("Helvetica", 12, "bold"), highlightthickness=0, command=update_details)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=12, bg=GREY, fg=GREEN, font=("Helvetica", 12, "bold"), highlightthickness=0, command=search_details)
search_button.grid(row=1, column=2)

window.mainloop()