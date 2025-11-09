from tkinter import * 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_img)
logo.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")  # Align right

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0, sticky="E")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")  # Stretch horizontally

email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2, sticky="EW")

password_output = Entry(width=21)
password_output.grid(row=3, column=1, sticky="EW")

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, sticky="EW", padx=(5,0))

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
