#Random module 
import random
import my_module

# random_integer = random.randint(1,10)
# print(random_integer)

"""What is a module? A module is a small part of the program that is responsible for a certain functionality, but how do
we create our own module?"""

# print(my_module.my_fav_number)

#How do we generate a random floating point numbers? Using the random.random() module 

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

#Lets create a program that will print heads or tails 

# coin_flip = random.randint(0,1)

# if coin_flip == 1:
#     print("heads")
# else:
#     print("tails")

"""Python lists, this is what you would call a data structure. What does this mean? It's just a way of storing and
organizing data in Python
Python lists are a set of square brackets, with many items stored inside and those items can be any data type
For example, this is a list  
fruits = [item1, item2]

We can append items to a list using the append function to the end of the list for example 
fruits.append("apple")"""

#IndexErrors and Working with Nested Lists

"""One of the most common error when working with lists is the IndexError: list index out of range
What does this mean? - basically means the list index is too small for this range"""
#How can we have lists inside a list? 
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)