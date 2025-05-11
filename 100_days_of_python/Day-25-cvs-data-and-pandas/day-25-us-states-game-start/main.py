import turtle
import pandas


def guess_state(state_guess):
    """This functions takes the users guess, and opens the csv file to pull the data from the csv file"""
    #Take the state_guess if it exists, return the x and y coordinates 
    state_x_y = data[data.state == state_guess]
    if state_x_y.empty:
        return None
    elif not state_x_y.empty:
        x_coord = state_x_y.x
        y_coord = state_x_y.y
        return int(x_coord), int(y_coord)

def write_state_to_screen(x_coord,y_coord,state):
    """This function writes the state to the map"""
    state_turtle.hideturtle()
    state_turtle.penup()
    state_turtle.goto(x_coord,y_coord)
    state_turtle.write(arg=state)


screen = turtle.Screen()
screen.title = ("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_turtle = turtle.Turtle()
#Open the csv file 
data = pandas.read_csv("./50_states.csv") #This will be a pandas.core.frame.DataFrame

amount_of_states = len(data.state)

correct_guesses = 0 
states_guessed = []


game_over = False
while not game_over:

    answer_state = screen.textinput(prompt="What's another state's name", title=f"{correct_guesses}/{amount_of_states} States Correct").title()

    #Store the result of the function guess_state 
    result = guess_state(answer_state)
    if result and (result not in states_guessed):
    #Return the x and y coordinate of state guessed if the result is not empty  
        x_coord, y_coord = result
        states_guessed.append(answer_state)
        #Write the guess on the map 
        write_state_to_screen(x_coord,y_coord,answer_state)
        correct_guesses += 1 
        #Track how many states we guess correctly vs the number of states left, and record the correct guesses in a list 

    if correct_guesses == amount_of_states:
        print("Congrats you guessed all the states")
        game_over = True
    

screen.mainloop()
screen.exitonclick()