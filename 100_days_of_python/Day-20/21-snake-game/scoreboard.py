from turtle import Turtle
ALIGN = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=270)
        self.write(arg=f"Score: {self.score}", align= ALIGN,font =("Arial",24,"normal"))
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align= ALIGN,font =("Arial",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align=ALIGN,font =("Arial",24,"normal"))