from turtle import Turtle
ALIGN = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=270)
        self.update_scoreboard()
    
    def add_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align= ALIGN,font =("Arial",24,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    
    def read_highscore(self):
        with open("data.txt") as file:
            high_score = file.read()
            return int(high_score)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", align=ALIGN,font =("Arial",24,"normal"))
            
