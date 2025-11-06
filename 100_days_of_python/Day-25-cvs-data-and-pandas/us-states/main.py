import turtle 
import pandas as pd

#Turtle screen settings 
screen = turtle.Screen() 
screen.title = ("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Import the csv data of states 
data = pd.read_csv("50_states.csv")

#Cursor configuration for marking states 
cursor = turtle.Turtle()
cursor.hideturtle()

score = 0 
correct_guesses = []
TOTAL_STATES = len(data)

while score != TOTAL_STATES:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
    guess = data[data["state"] == answer_state]
    if answer_state == "Exit":
        screen.bye()
        break
    elif answer_state in correct_guesses: 
        print("You already guessed this.")
    elif not guess.empty:
        cursor.penup()
        #If i am converting a variable to a specific type document why this needs to occur. 
        cursor.goto(x=int(guess.x.iloc[0]), y=int(guess.y.iloc[0]))
        cursor.write(answer_state)
        correct_guesses.append(answer_state)
        score += 1 
    else:
        print("Guess again")

#Find the missing states if a user exits early 

correct_answers = pd.Series(correct_guesses)

combined_answers = pd.concat([correct_answers,data["state"]])
leftover_answers = combined_answers.drop_duplicates(keep=False)


screen.exitonclick() 