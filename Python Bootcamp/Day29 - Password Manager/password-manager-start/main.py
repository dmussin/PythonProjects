from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_output.insert(0, password)

    # Copy password to a clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    web = str(website_input.get())
    user = str(username_input.get())
    password = str(password_output.get())

    # Empty filed trigger
    if len(web) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showwarning(title="Oops", message="Please fill the fields!")
    else:
        # Pop-up window
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered:"
                                                          f"\nEmail:{user} "
                                                          f"\nPassword: {password} "
                                                          f"\nIs it ok to save?)")
        if is_ok:
            file = open("data.txt", "a")
            file.write(f"{web} | {user} | {password}\n")
            file.close()

            website_input.delete(0, END)
            password_output.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Courier", 16))
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:", font=("Courier", 16))
username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Courier", 16))
password_label.grid(column=0, row=3)

# Buttons
generate_button = Button(text="Generate Password", font=("Courier", 15), command=generate_password)
generate_button.grid(column=2, row=3)


add_button = Button(text="Add", font=("Courier", 15),
                         highlightthickness=1, width=41, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# Entry fields
website_input = Entry(width=44)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

username_input = Entry(width=44)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "dan4ik377@gmail.com")

# Password Output
password_output = Entry(width=23)
password_output.grid(column=1, row=3)

window.mainloop()