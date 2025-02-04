"""
OOP - Object oriented programming. 
Procedural programming where the computer works from top to bottom jumping out into a function as needed. (This is what we have been 
doing)
As the code gets more and more complicated the # of relationships needed to remember and manage becomes hetic. 
This is where OOP comes in

OOP consists of classes, attributes and methods 

Classes are like a blueprint which tells us 
what features the object will have (attributes) 
What actions it can do (methods )

Benefits of OOP 
1. Classes can be reused to create multiple objects without writing the same code repeatedly 
2. Better organization & Scalability, OOP groups attributes and methods together 
3. Encapsulation hides internal details of an object and only exposes what's necessary 
"""

#Constructing objects and accessing their attributes 
"""Classes are named in Pascal Case for example CarBlueprint()
Ex object = Class 
car = CarBlueprint()
"""

# import turtle 

# #This is a new object named timmy thats using the class Turtle 
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.color("red")

# #What can we do in this object? 

# my_screen = turtle.Screen() #<- object 
# print(my_screen.canvheight) #<- attribute 

# #We can pull a function(method) inside the class 
# my_screen.exitonclick()

#pypi.org Python package index, software for python developed by the Python community 

#Practicing modifying object attributes and calling methods 
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokeman Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)