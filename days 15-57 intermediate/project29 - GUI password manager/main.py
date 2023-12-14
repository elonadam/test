from tkinter import *

GREY = '#BBBBBB'
LIGHT_GREY = '#E2D5D5'


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

# TODO 1 save the user input to data.txt file by clicking the add button
# TODO 2 to clear the input after add button pressed

def save_to_file():
    """Getting tuple input and append that in a text file"""
    user_set = add_pass()  # get input
    with open("C:/Users/USER/Documents/pycharmProjects/day29/data.txt", "a") as file:
        file.write(user_set)
    clear_input(website_input)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Pass Manager")
# window.minsize(width=200, height=200)
window.config(padx=50, pady=50, bg=LIGHT_GREY)

canvas = Canvas(width=220, height=220, bg=LIGHT_GREY, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", bg=LIGHT_GREY, highlightthickness=0)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg=LIGHT_GREY, highlightthickness=0)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg=LIGHT_GREY, highlightthickness=0)
password_label.grid(row=3, column=0)

# Entries

website_input = Entry(width=35)
# web_data = website_input.get()
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.insert(END, string="elon@python3.com")
# email_data = email_input.get()
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=16)
# pass_data = password_input.get()
password_input.grid(row=3, column=1, columnspan=1)


# Buttons
def clear_input(entry_name):
    entry_name.delete(0, END)


def add_pass():
    web_data = website_input.get() # Get input from the entry field
    email_data = email_input.get()
    pass_data = password_input.get()
    new_set = f"{web_data} | {email_data} | {pass_data} \n" # Storing collected data in tuple
    #print("from add_pass", new_set)
    return new_set


generate_button = Button(text="Generate Passwords", bg=LIGHT_GREY, width=15, command=generate_pass)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", bg=LIGHT_GREY, width=30, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
