import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)

    psw = "".join(password_list)

    passInput.insert(0, psw)
    pyperclip.copy(psw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = webInput.get().strip().title()
    username_data = userInput.get().strip()
    password_data = passInput.get().strip()
    new_data = {
        website: {
            "username": username_data,
            "password": password_data,
        }
    }

    if not website or not password_data:
        messagebox.showerror(title="Validation failed", message="Please fill in both website and password fields")
    else:
        try:
            with open("data.json") as file:
                data = json.load(file)
        except FileNotFoundError as error:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                data.update(new_data)
                json.dump(data, file, indent=4)  # Correct the order of arguments
        finally:
            webInput.delete(0, END)
            passInput.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


def find_password():
    search_str = webInput.get().strip().title()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="404", message="No Data found")
    else:
        if search_str in data:
            email = data[search_str]["username"]
            password = data[search_str]["password"]
            messagebox.showinfo(title=email, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showerror(title="404", message="No Data found for that site")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(width=500, height=500, padx=20, pady=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(110, 110, image=photo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website", font=("Times New Roman", 14))
webInput = Entry(width=21)
website.grid(column=0, row=1)
webInput.grid(column=1, row=1)

username = Label(text="Username/Email", font=("Times New Roman", 14))
userInput = Entry(width=35)
username.grid(column=0, row=2)
userInput.grid(column=1, row=2, columnspan=2)

password = Label(text="Password", font=("Times New Roman", 14))
passInput = Entry(width=21)
pswGenerate = Button(width=9, text="Generate", command=generate_password)
password.grid(column=0, row=3)
passInput.grid(column=1, row=3)
pswGenerate.grid(column=2, row=3)

search_btn = Button(text="Search", width=10, command=find_password)
search_btn.grid(row=1, column=2)
addBtn = Button(width=33, text="Add", command=save_password)
addBtn.grid(column=1, row=4, columnspan=2)
window.mainloop()
