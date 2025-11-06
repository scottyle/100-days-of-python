from tkinter import *

def button_clicked():
    """Shows "Button Got Clicked" on my_label when the button is clicked"""
    my_label.config(text=input.get())

window = Tk()
window.title(string="My First GUI program")
window.minsize(width=600,height=300)
window.config(padx=20,pady=20)

#Label
my_label = Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)

#Button 
button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)

#New button 
new_button = Button(text="New Button")
new_button.grid(column=2,row=0)

#Entry 
input = Entry(width=100)
input.grid(column=3,row=3)







window.mainloop()