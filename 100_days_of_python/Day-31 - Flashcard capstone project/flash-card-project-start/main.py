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

# ----------------------------CREATE NEW FLASHCARDS ------------------------------- #
def create_new_flash_cards():
    try: 
        df = pd.read_csv(FRENCH_WORDS_DATA)
    except FileNotFoundError as e:
        print(e)
    else:
        words = df.to_dict()
        length_of_french_words = len(words["French"])
        #Loop through dict to get both french words and english words 
        canvas.itemconfigure(title_text,text="French")
        canvas.itemconfigure(word_text,text=words["French"][random.randrange(0,length_of_french_words)])

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(string="Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file=CARD_FRONT_IMG)
canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

title_text = canvas.create_text(400,150, text="Title",font=(FONT_NAME,40))
word_text = canvas.create_text(400,263,text="Word", font=(FONT_NAME,60,"bold"))

#Buttons
right_img = PhotoImage(file=RIGHT_IMG)
right_button = Button(image=right_img, highlightthickness=0,command=create_new_flash_cards)
right_button.grid(row=1,column=1)

wrong_img = PhotoImage(file=WRONG_IMG)
wrong_button = Button(image=wrong_img,highlightthickness=0,command=create_new_flash_cards)
wrong_button.grid(row=1,column=0)



window.mainloop()   