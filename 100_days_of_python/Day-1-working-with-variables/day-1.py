#Day 1 

#Strings is a series of characters, surrounded by single or double quotes.
#To print a string in Python, we use the print() function.
#Example: 

print("Hello World")

# Fix the code below 👇

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

# What if we wanted to enter some data from the user?
# We can use the input() function to get input from the user.
# Example:

name = input("What is your name? ")
print("Hello " + name)

# How did we capture the input from the user?
# Using variables in Python. Variables are used to store data values.

glass1 = "milk"
glass2 = "juice"
#Switch the contents of glass1 and glass2
glass1, glass2 = glass2, glass1 
print("Glass 1: " + glass1 + "\n" + "Glass 2: " + glass2)
"""
Basic rules for naming variables in Python:
1. Must start with a letter or an underscore (_):

2. Valid: myVar, _myVar
    Invalid: 1myVar
    Can contain letters, numbers, and underscores:

    Valid: my_var1, var_2
    Invalid: my-var, my var

3. Case-sensitive:

    myVar and myvar are different variables.

4. Cannot be a reserved keyword:

    Keywords like False, class, return, None, etc., cannot be used as variable names.
5. Should be descriptive and meaningful:

    Prefer user_age over ua.
"""