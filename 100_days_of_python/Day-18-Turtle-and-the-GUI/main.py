from turtle import Turtle, Screen
import random 

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("orange4")
# timmy_the_turtle.pensize(10)
# timmy_the_turtle.speed(5)

#Draw multiple types of shapes 
# draw_shapes = True
# sides_of_shape = 3

# while draw_shapes:
#     for _ in range(sides_of_shape):
#         timmy_the_turtle.right(360/sides_of_shape)
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.color(random.choice(['red','blue','yellow','green',]))
#     sides_of_shape += 1
#     if sides_of_shape >= 10:
#         draw_shapes = False

# #Draw a random walk
# def random_walk(walk):
#     if walk == 1:
#         timmy_the_turtle.forward(50)
#     elif walk == 2:
#         timmy_the_turtle.right(90)
#     elif walk == 3:
#         timmy_the_turtle.left(90)
#     elif walk == 4:
#         timmy_the_turtle.backward(50)


# for _ in range(100):
#     timmy_walk = random.randint(1,4)
#     timmy_the_turtle.color(random.choice(['red','blue','yellow','green']))
#     random_walk(timmy_walk)

# directions = [0,90,180,270]

# for _ in range (200):
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#     timmy_the_turtle.color(random.choice(['red','blue','yellow','green']))

#Draw a square. 
# for _ in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)

#Draw a dashed line 
# for _ in range(50):
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.pendown()

# Draw a triangle 
# for _ in range (3):
#     timmy_the_turtle.right(120)
#     timmy_the_turtle.forward(100)

"""
Python tuples and how to generate random RGB colours 
"""
screen = Screen()
screen.exitonclick()

