from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self,start_position_x,start_position_y):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=start_position_x,y=start_position_y)
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
    
    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(),new_y)