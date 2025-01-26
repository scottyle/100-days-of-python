#Dictionaries 
"""Syntax for dictionaries look like this 
{ key : value }
ensure when calling a key from the dictionary that its spelled correctly or you'll get a key error
"""

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

#How would we programattically add a entry to the dictionary? 
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

#How do we wipe out an existing dictionary? 

# programming_dictionary = {}
# print(programming_dictionary)

#How do we edit an dictionary? Note if the value isnt found in the dictionary it will create a new entry in the dictionary
# programming_dictionary["Bug"] = "New value"

# print(programming_dictionary)

#How do we loop in a dictionary?

# for thing in programming_dictionary:
#     #This will print only the key's of the dictionary, if we wanted the values as well this is how we would do it 
#     print(thing)
#     print(programming_dictionary[thing])

#Nesting 
"""
Nested lists in dictionaries, we are able to represent more complex data in dictionaries 
"""

# travel_log = {
#     "France" : ["Paris", "Lillie", "Dijon"],
#     "Germany" : ["Stuttgart" , "Berlin"],
# }

#How would we print the Lillie string in this dictionary above?

# print(travel_log["France"][1])

#How would we print out the "D" in this nested list?
# nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

#We can have a nested dictionary inside a dictionary.
#How would we print out Stuttgart from this dictionary 
travel_log = {
    "France" : {
        "cities_visted" : ["Paris", "Lillie", "Dijon"],
        "total_visits" : 12,
    },

    "Germany" : {
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 12,
    },
}
print(travel_log["Germany"]["cities_visited"][2])