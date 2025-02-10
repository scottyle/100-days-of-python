#When a user taps a specific key on the keyboard and we're able to listen to what the user does this is known as a 
#event listener 

from turtle import Turtle,Screen

tim = Turtle()
screen = Screen() 

def move_forwards():
    tim.forward(10)

screen.listen() 
#This is a function being used as inputs 
"""
Ex.
def function_a(something):
    #Do this with something 
    #Then do this 
    #Finally do this 

def function_b()
    #Do this 

function_a(function_b)

"""
#Higher order function a function that can work with other functions
"""If we're using a function that we haven't its best practice to use keyword arguments instead of positional arguments
Why? 
Improves readability each argument is clear and easier to folow 
Handles default values better 
Avoids errors with argument order 
Handles API changes more robustly, if a function signature changes keyword arguments reduce that risk. 
"""
screen.onkey(key="space",fun=move_forwards)

screen.exitonclick()

"""
Object state and instances 

We can create many objects from the same class for example we have the following 
timmy = Turtle()
tommy = Turtle() 

Even though both timmy and tommy are turtle objects they function independently from each other, known as a instance 
What does this mean though? That means at any moment in time they could have different attributes and be doing different things 
The fact that each of these objects can have different attributes and be performing different methods is known as their "state"
"""
