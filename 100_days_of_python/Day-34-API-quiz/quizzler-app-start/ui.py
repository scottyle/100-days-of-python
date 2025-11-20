from tkinter import *

TRUE_BUTTON = "images/true.png"
FALSE_BUTTON = "images/false.png"
THEME_COLOR = "#375362"
FONT = "Arial"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2,padx=20,pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="hello",
            font=(FONT,20,"italic")
        )

        self.true_img = PhotoImage(file=TRUE_BUTTON)
        self.true_button = Button(image=self.true_img,highlightthickness=0)
        self.true_button.grid(row=2,column=0)

        self.false_img = PhotoImage(file=FALSE_BUTTON)
        self.false_button = Button(image=self.false_img,highlightthickness=0)
        self.false_button.grid(row=2,column=1)

        self.score_label = Label(text="Score: 0", font=(FONT),bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=0,column=1)

        self.window.mainloop()

        