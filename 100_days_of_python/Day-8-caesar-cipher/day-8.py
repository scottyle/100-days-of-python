#Functions with inputs 

# def greet():
#     print("Hello World")
#     print("Hello again")
#     print("I'm a function")

# greet()

#Functions with inputs 
"""
def my_function(something):
    #Do this with something 
    #Then do this 
"""

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"Hello again {name}")
#     print("I'm a function")

# greet_with_name("Scott")

"""
something = 123
parameter / argument 
The argument is whats being passed into the function whereas the parameter is the name of that data 
"""

#Positional vs keyword arguments 

#Functions with more than 1 input 

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

"""The default way of calling functions is positionals, basically we havent associated the pieces of data with something,
so it performs the default way of calling functions, what if we wanted to never occurr this problem where we have to worry
about the position of the parameters. 
We could use something called Keyword arguments instead  
"""
greet_with("Scott", "Mississauga")

#Keyword arguments 
greet_with( location= "Toronto", name = "Karleigh")

# def calculate_love_score(name1 , name2):
    
#     combined_name = (name1 + name2).upper()
#     true = ["T", "R", "U", "E"]
#     love = ["L", "O", "V", "E"]
#     true_counter = 0
#     love_counter = 0
    
#     for letters in combined_name:
#         if letters in true:
#             true_counter += 1 
#         if letters in love:
#             love_counter += 1 

#     total_counter = str(true_counter) + str(love_counter)
#     print(f"{total_counter}")

# calculate_love_score("Kanye West", "Kim Kardashian")


fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(len(alphabet))