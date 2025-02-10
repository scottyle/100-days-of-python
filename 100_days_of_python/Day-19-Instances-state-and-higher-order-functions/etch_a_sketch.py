"""
Create a Etch-A-Sketch app that performs the following 
W = Forwards
S = Backwards 
A = Counter-clockwise 
D = Clockwise 
C = Clear drawing 
"""

from turtle import Turtle, Screen

def move_forward():
    turtle.forward(5)

def move_backward():
    turtle.backward(5)

def move_clockwise():
    turtle.right(5)

def move_c_clockwise():
    turtle.left(5)

def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

def etch_a_sketch(screen,key):
    for key_bindings, func in key.items(): 
        screen.onkey(fun=func,key=key_bindings)

#Intialize classes to be used 
screen = Screen() 
turtle = Turtle() 


screen.listen() 

key_bindings = {
    "w" : move_forward,
    "s" : move_backward,
    "d" : move_clockwise,
    "a" : move_c_clockwise,
    "c" : clear_screen,
}

etch_a_sketch(screen,key_bindings)




#Exit the screen on click 
screen.exitonclick() 