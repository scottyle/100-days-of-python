from turtle import Turtle, Screen
import random 
screen = Screen()

screen.setup(width=500,height=400)

#Make a popup to ask the user who will win 
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
list_of_turtles = []
is_race_on = False 

def make_turtle():
    for turtle_color in colors:
        new_turtles = Turtle(shape="turtle")
        new_turtles.color(turtle_color)
        list_of_turtles.append(new_turtles)

def start_position():
    #X and Y coordinates
    start_y = -100
    start_x = -230 
    for turtles in list_of_turtles:
        turtles.penup()
        turtles.goto(x=start_x,y=start_y)
        start_y += 30

if user_bet:
    is_race_on = True 

make_turtle()
start_position()

while is_race_on:
    for turtle in list_of_turtles:
    #Loop will end once a turtle has reached the 230 x coordinate mark 
        if turtle.xcor() > 230:
            is_race_on = False 
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning color is {winning_color}")
            else:
                print(f"You lose. The winning color {winning_color}")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()