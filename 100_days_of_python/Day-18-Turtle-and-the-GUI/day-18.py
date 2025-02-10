#Basic import statement for example 
import turtle
tim = turtle.Turtle()

#A much more conveninent way of doing it would be to do this 
#keyword | modulename |  keyword | thing in module 
from       turtle        import    Turtle
#This way we dont need to keep writing turtle.Turtle() when making a class 
tim = Turtle()

#Another way of importing everything we want is by using the asterisk 

from turtle import * 
"""
This has its advantages and disadvantages, because it can make it really hard to see where each of these classes or 
methods come from. Dont do the asterisk because later down the road it will make the code really confusing to follow through
because you're importing a lot of modules. Instead if you're using a module many times use the "from import" statement 
if we're only using it once use the "import" statement 
"""

#Alias modules for example we can import turtle as t 
import turtle as t
tim = t() 

"""
Installing modules, just an FYI there are some modules you cannot just import 
"""

"""
Python tuples is a data type in Python. Whats the difference between a tuple and list?
A tuple is craved in stone therefore you cant change it, this is known as immutable 
Ex my_tuple = (0,5,8)
"""