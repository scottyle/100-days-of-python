#Tips and techniques for debugging 

"""
1. Describe the problem in your head - make sense of whats going on 

"""

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")


# my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#For loop is looping through a range of numbers between 1 and 20
# 2. When is the function meant to print "You got it"?
#Function is suppose to print you got it when i equals 20
# 3. What are your assumptions about the value of i?
#The assumption of the value i is that its suppose to go to 20, but it doesn't since it stops at 19

"""
2. Reproduce the bug, because when you encounter it once and don't encounter it again it becomes a difficult bug to fix 

"""

#Reproduce the bug so that it always produces the error 
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # dice_num = randint(1, 5)
## dice_num = 6
# print(dice_images[dice_num])

"""
3. Play computer 

Play computer and go through the code line by line as if you were executing the code to figure out why 1994 does not work as expected. 
Then go ahead and fix the code.
"""

# year = int(input("What's your year of birth?"))

# #Issue with this code is that theres no validation for year equaling to 1994.

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

"""
4. Fix the errors before continuing 
"""
# We can use a try - except block 

# #Lets rewrite the code to include a try except block
# try:
#     age = int(input("How old are you?"))
# except ValueError: #What should happen if we end up with this error
#     print("You didn't enter a number")
#     age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
# #What if we input age = twelve this would cause this error - ValueError: invalid literal for int() with base 10: 'twelve'

"""
5. Use the print statement
"""

"""
6. Use the debugger 
Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging. 
This is normally known as the debugger. In many ways, they are like print statements on steroids.

Debuggers allows us to peek into our code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.

There are a couple of things that are the same in most IDEs which you should be familiar with:

Breakpoint - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). 
This line will be where the program pauses during debug run.

Step Over - This button will go through the execution of your code line by line and allow you to view the intermediate values of your variables.

Step Into - This will enter into any other modules that your code references. 
e.g. If you use a function from the random module it will show you the original code for that function so you can better understand its functionality and how it relates to your problems.

Step Into My Code - This does the same thing as Step Into, but it limits the scope to your own project code and ignores library code such as random.

PAUSE 1
Use the PyCharm debugger to figure out what is the issue in the starting code and fix it.
"""

import random
import math


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = math.add(new_item, item)
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
