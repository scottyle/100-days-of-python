from tkinter import *

def button_clicked():
    """Shows "Button Got Clicked" on my_label when the button is clicked"""
    my_label.config(text=input.get())

window = Tk()
window.title(string="My First GUI program")
window.minsize(width=600,height=300)

#Label
my_label = Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.pack()

my_label.config(text="New Text")

#Button 
button = Button(text="Click me", command=button_clicked)
button.pack()

#Entry 
input = Entry(width=100)
input.pack()







window.mainloop()