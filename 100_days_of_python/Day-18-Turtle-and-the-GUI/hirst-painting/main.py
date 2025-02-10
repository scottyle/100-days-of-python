import random
from turtle import Turtle, Screen

def move_position(x,y):
    """This function starts the cursor at the bottom left corner """
    cursor.penup()
    cursor.goto(x,y)
    cursor.pendown()

def hirst_painting():
    """This function draws 10 by 10 dots along each side, dots should be 20 in size and spaced apart by around 50 paces """
    start_x = -screen.window_width() // 2 + 50  
    start_y = -screen.window_height() // 2 + 50  

    for row in range(10):  # 10 rows
        for column in range(10):  # 10 columns
            move_position(start_x + (column * 50), start_y + (row * 50)) 
            cursor.dot(20, random.choice(color_list))

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

#Initalize the screen and Turtle class 
screen = Screen()
cursor = Turtle()
cursor.speed('fastest')

#Set the screen size 
screen.setup(625,625)
screen.colormode(255)

hirst_painting()

screen.exitonclick()

