from tkinter import * 
from tkmacosx import Button
import math 

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    tracker.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else: 
        count_down(work_sec)
        timer_label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec <= 9: 
        count_sec = f"0{count_sec}"
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else: 
        start_timer()
        if REPS % 2 == 0: 
            tracker.config(text="✅" * int(REPS/2))
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomorodo timer")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill = "white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

timer_label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME,100,"bold"))
timer_label.grid(row=0,column=1)

start_button = Button(text="Start",bg=YELLOW,activebackground=YELLOW,borderless=1,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",bg=YELLOW,activebackground=YELLOW,borderless=1,command=reset_timer)
reset_button.grid(row=2,column=3)

tracker = Label(text="",fg=GREEN,bg=YELLOW)
tracker.grid(row=3,column=1)

window.mainloop()
