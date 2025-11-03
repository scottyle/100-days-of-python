import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label 
my_label = tkinter.Label(text="I Am A Label", font=("Arial",24,"bold"))
my_label.pack(side="bottom")

"""
Setting default values for optional argument inside a function header
"""


window.mainloop()
