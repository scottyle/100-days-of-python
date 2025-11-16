from tkinter import *
import pandas as pd 
import random
import sys
from tkinter import messagebox

FRENCH_WORDS_DATA = "data/french_words.csv"
WORDS_TO_LEARN = "data/words_to_learn.csv"
RIGHT_IMG = "images/right.png"
WRONG_IMG = "images/wrong.png"
CARD_BACK_IMG = "images/card_back.png"
CARD_FRONT_IMG = "images/card_front.png" 
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

flip_timer = None

# ---------------------------- CREATE NEW FLASHCARDS ------------------------------- #
def next_flash_card(right_or_wrong):
    global flip_timer
    try:
        current_card = random.choice(words)
    except IndexError as e:
        messagebox.showinfo(title="Congrats!",message="No words left! Exiting game.")
        sys.exit(1)

    canvas.itemconfig(canvas_image,image=card_front_img)
    canvas.itemconfig(title_text,text="French",fill="black")
    canvas.itemconfig(word_text,text=current_card["French"],fill="black")

    # Cancel any pending flip before scheduling a new one
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    if right_or_wrong == "right":
        words.remove(current_card)
        words_left_over = pd.DataFrame(words)
        words_left_over.to_csv(WORDS_TO_LEARN,index=False)

    flip_timer = window.after(3000,lambda: flip_card(current_card["English"]))


# ---------------------------- FLIP CARD TO ENGLISH WORD ------------------------------- #
def flip_card(current_word):
    canvas.itemconfig(canvas_image,image=card_back_img)
    canvas.itemconfig(title_text,text="English", fill="white")
    canvas.itemconfig(word_text,text=current_word,fill="white")

# ---------------------------- READ DATA OF WORDS ------------------------------- #
    
#Read words_to_learn.csv 

try: 
    df = pd.read_csv(WORDS_TO_LEARN)
    words = df.to_dict(orient="records")
except FileNotFoundError as e:
    try: 
        df = pd.read_csv(FRENCH_WORDS_DATA)
        words = df.to_dict(orient="records")
        print("No words_to_learn.csv file found opening french_words.csv")
    except FileNotFoundError as e:
        print("Cannot find the french_words.csv file. Exiting...")
        sys.exit(1)      
# ---------------------------- UI SETUP ------------------------------- #
#Run only if the csv file does not throw an error. 

window = Tk()
window.title(string="Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file=CARD_FRONT_IMG)
card_back_img = PhotoImage(file=CARD_BACK_IMG)
canvas_image = canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

title_text = canvas.create_text(400,150, text="Title",font=(FONT_NAME,40))
word_text = canvas.create_text(400,263,text="Word", font=(FONT_NAME,60,"bold"))

next_flash_card("start")

#Buttons
right_img = PhotoImage(file=RIGHT_IMG)
right_button = Button(image=right_img, highlightthickness=0,command=lambda:next_flash_card("right"))
right_button.grid(row=1,column=1)

wrong_img = PhotoImage(file=WRONG_IMG)
wrong_button = Button(image=wrong_img,highlightthickness=0,command=lambda:next_flash_card("left"))
wrong_button.grid(row=1,column=0)


window.mainloop()   