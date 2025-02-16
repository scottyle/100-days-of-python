from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0 
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-280,250)
        self.write(f"Level:{self.score}",font=FONT)
    
    def game_over(self):
        self.clear()
        self.goto(-200,0)
        self.write("GAME OVER",move="center",font=("Courier", 80, "normal"))
