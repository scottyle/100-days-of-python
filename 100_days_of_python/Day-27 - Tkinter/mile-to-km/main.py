from tkinter import *
MILES_TO_KM_RATIO = 1.609344

def mile_to_km():
    """
    Desktop application for taking miles and converting it to KM
    """
    try:
        miles = entry.get()
        miles_to_km = round((float(miles) * MILES_TO_KM_RATIO),2)
        km_result_label.config(text=str(miles_to_km))
    except ValueError:
        km_result_label.config(text="Please input a valid number")


#Window configuration 
window = Tk()
window.title(string="Mile to Km Converter")
window.config(padx=20,pady=20)

#Entry 
entry = Entry(width=10)
entry.grid(column=1,row=0)

#Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

#IsEqualTo
is_equal_to = Label(text="is Equal to")
is_equal_to.grid(column=0,row=1)

#Output label 
km_result_label = Label(text="0")
km_result_label.grid(column=1,row=1)

#KM label 
km = Label(text="Km")
km.grid(column=2,row=1)

#Calculate button
calculate = Button(text="Calculate",command=mile_to_km)
calculate.grid(column=1,row=2)

window.mainloop()