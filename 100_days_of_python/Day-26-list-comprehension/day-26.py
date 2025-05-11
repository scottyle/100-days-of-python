"""
List comprehension is where you create a new list from a previous list 

Syntax would look like this 
new_list = [ new_item for item in list ]

Just because its list comprehension doesnt mean you can only work with lists, you can also work with strings 
"""
# numbers = [1,2,3]
# new_list = [ n+1 for n in numbers]
# print(new_list)

# name = "Scott"
# new_list = [letter for letter in name]
# print(new_list)

#Challenge create a new list from a range where the list items are double the values in the range 
# range = range(1,5)
# double_range = [n*2 for n in range]
# print(double_range) 

"""
Conditional list comprehension 
Syntax 
new_list = [ new_item for item in list if test ]
Basically means that only to perform if the test passes 
"""

#Create a new list that contains the names longer than 5 characters in ALL CAPS
names = ["Alex", "Beth", "Caroline", "Dave", "Elenaor", "Freddie"]

names_in_upper = [name.upper() for name in names if len(name) >=5]
print(names_in_upper)