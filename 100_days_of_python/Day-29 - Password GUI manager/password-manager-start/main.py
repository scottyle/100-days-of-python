from tkinter import * 
from tkinter import messagebox
import random
import pyperclip
import json
from validation.validation import check_email

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
DEFAULT_EMAIL = "testingemail@outlook.com"
LOGO = "logo.png"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    password_input.delete(0,END)
    password_list = [random.choice(SYMBOLS) for char in range(random.randint(2, 4))] + [random.choice(NUMBERS) for char in range(random.randint(2, 4))] + [random.choice(LETTERS) for char in range(random.randint(8, 10))]
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0,string=password)
    pyperclip.copy(text=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    file_name = "data.json"

    #Check if email inputted a correct email
    is_email_valid = check_email(email)

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error",message="Please don't leave any fields empty!")
        
    elif is_email_valid:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website}\nEmail: {email} \nIs it okay to save?")

        login_info = {
            website : {
                "email" : email,
                "password" : password
            }
        }

        #Check if website entry/email already exists if so prompt user to overwrite 
        if is_okay:
            try: 
                with open(file_name, "r") as passwords_file:
                    data = json.load(passwords_file)
            except FileNotFoundError:
                print("File not found.")
                data={}
            
            data.update(login_info)

            with open(file_name,"w") as json_file:
                json.dump(data,json_file, indent=4)

            #Clear input after saving        
            password_input.delete(0,END)
            website_input.delete(0,END)
    
    else:
            messagebox.showwarning(title="Incorrect Entry!", message="Input a correct email please.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = Canvas(width=200, height=200)
logo_img = PhotoImage(file=f"{LOGO}")
logo.create_image(100, 100, image=logo_img)
logo.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0, sticky="E")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW") 
website_input.focus()

email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_username_input.insert(0,string=f"{DEFAULT_EMAIL}")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW", padx=(5,0))

add_button = Button(text="Add", width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
