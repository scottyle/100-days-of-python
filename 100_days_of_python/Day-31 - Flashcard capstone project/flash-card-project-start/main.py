from tkinter import *
import pandas as pd 
import random

FRENCH_WORDS_DATA = "data/french_words.csv"
RIGHT_IMG = "images/right.png"
WRONG_IMG = "images/wrong.png"
CARD_BACK_IMG = "images/card_back.png"
CARD_FRONT_IMG = "images/card_front.png" 
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

flip_timer = None

# ---------------------------- CREATE NEW FLASHCARDS ------------------------------- #
def create_new_words():
    global flip_timer
    current_card = random.choice(words)

    canvas.itemconfig(canvas_image,image=card_front_img)
    canvas.itemconfig(title_text,text="French",fill="black")
    canvas.itemconfig(word_text,text=current_card["French"],fill="black")

    # Cancel any pending flip before scheduling a new one
    if flip_timer is not None:
        window.after_cancel(flip_timer)
        words.remove(current_card)

    flip_timer = window.after(3000,lambda: flip_card(current_card["English"]))

# ---------------------------- FLIP CARD TO ENGLISH WORD ------------------------------- #
def flip_card(current_word):
    canvas.itemconfig(canvas_image,image=card_back_img)
    canvas.itemconfig(title_text,text="English", fill="white")
    canvas.itemconfig(word_text,text=current_word,fill="white")

# ---------------------------- READ DATA OF WORDS ------------------------------- #
try: 
    df = pd.read_csv(FRENCH_WORDS_DATA)
    words = df.to_dict(orient="records")
except FileNotFoundError as e:
    print("Cannot find the french_words.csv file.")
        
# ---------------------------- UI SETUP ------------------------------- #
#Run only if the csv file does not throw an error. 
else:
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

    create_new_words()

    #Buttons
    right_img = PhotoImage(file=RIGHT_IMG)
    right_button = Button(image=right_img, highlightthickness=0,command=create_new_words)
    right_button.grid(row=1,column=1)

    wrong_img = PhotoImage(file=WRONG_IMG)
    wrong_button = Button(image=wrong_img,highlightthickness=0,command=create_new_words)
    wrong_button.grid(row=1,column=0)
    breakpoint()

    window.mainloop()   