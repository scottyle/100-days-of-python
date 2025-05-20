import turtle 
import pandas 

screen = turtle.Screen()

screen.title("U.S States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


#Check if the guess is among the 50 states 
states = pandas.read_csv("50_states.csv")

score = 0 
while score != len(states):
    answer_state = screen.textinput(title = "Guess the State", prompt= "What's another state's name?").title()
    answer = (states[states.state.str.contains(answer_state)])
    
    if not answer.empty:
        x_coord = answer.x
        y_coord = answer.y 
        state = answer.state
        score += 1 
    else:
        print("Incorrect")
breakpoint()