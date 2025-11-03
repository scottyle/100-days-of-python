# """
# List comprehension is where you create a new list from a previous list 
import random 
# Syntax would look like this 
# new_list = [ new_item for item in list ]

# Just because its list comprehension doesnt mean you can only work with lists, you can also work with strings 
# """
# # numbers = [1,2,3]
# # new_list = [ n+1 for n in numbers]
# # print(new_list)

# # name = "Scott"
# # new_list = [letter for letter in name]
# # print(new_list)

# #Challenge create a new list from a range where the list items are double the values in the range 
# # range = range(1,5)
# # double_range = [n*2 for n in range]
# # print(double_range) 

# """
# Conditional list comprehension 
# Syntax 
# new_list = [ new_item for item in list if test ]
# Basically means that only to perform if the test passes 
# """

# #Create a new list that contains the names longer than 5 characters in ALL CAPS
# names = ["Alex", "Beth", "Caroline", "Dave", "Elenaor", "Freddie"]

# names_in_upper = [name.upper() for name in names if len(name) >=5]
# print(names_in_upper)


"""
List comprehension:

What is list comprehension? 
A case where you create a new list from a previous list 
"""
#For example we would create a list from a previous list using the following 
# numbers = [1,2,3]
# new_list = []

# for n in numbers:
#     add_1 = n + 1 
#     new_list.append(add_1)

#We can take these lines of code and turn it into one 
"""
For example 

new_list = [new_item for item in list]
name of new list = [] <- square brackets to denote we're creating a new list 
Heres how it works 

"""
# numbers = [1,2,3]

# new_list = [n+1 for n in numbers]
# print(new_list)

# #We can with other sequences like strings for example 
# name = "Angela"
# #Predict what new_list will contain 
# new_list = [letter for letter in name]
# #Should contain A,n,g,e,l,a
# print(new_list)

# #Python Sequences consist of things like a list, string, range or tuple because when you perform a list comphrension its going to take that sequence and its going to go through it in order
# #If its a letters in a string or items in a list and do something with it 

# #Challenge - Create a new list from a range where the list items are double the values in the range 

# new_list = [n*2 for n in range(1,5)]
# print(new_list)

"""
Conditional list comprehension 
new_list = [new_item for item in list if test]
"""
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# #Challenge make a new list, for names that have 4 letters or less 
# names_list = [name for name in names if len(name)<= 4]
# print(names_list)
# #Challenge make a new list that contains the names longer than 5 characters in ALL CAPS
# caps_names = [name.upper() for name in names if len(name) > 5]
# print(caps_names)

"""
Dictionary Comprehension 
new_dict = {new_key:new_value for item in list}

We can also create a new dict based on the values in an existing dict

new_dict = {new_key:new_value for (key,value) in dict.items()}

Finally we can add a condition at the end 

new_dict = {new_key:new_value for (key,value) in dict.items() if test} 
"""

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)

# #Loop through a dict 
# passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
# print(passed_students)

"""
How to iterate over a pandas dataframe 

"""