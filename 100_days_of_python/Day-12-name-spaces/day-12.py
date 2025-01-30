#Scope 
"""Variables or functions declared in functions have a local scope they are only seen within the same block of code
Basically any variables/function declared in a function are only accessible in a function this is known as local scope
But what if wanted it to be accessible outside of the function?
Global scope the player health variable is a global variable because it was defined at the top level of the file
 
# """

# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")

# #Global scope 
# player_health = 10 

# def game()
#     def drink_health():
#         print(player_health)
#     drink_health()

# #This is giving a issue because the function drink_health is inside the local scope we have to define it in def game() for it to be called 
# drink_health()

"""There is no block scope in python, this means that variables created in other blocks of code, if, while loops don't 
get a local scope they are global scope 
"""

game_level = 3 
enemies = ["Skeleton", "Cow", "Orc"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


"""
You can force the code allow you to modify something with global if you use the global keyword before you use it.

e.g. This will give you an error

a = 1
def my_function():
    a += 1
    print(a)
But this will work

a = 1
def my_function():
    global a
    a += 1
    print(a)
    
You do not want to do this often where we modify the global scope because this becomes really confusing aka more easier to fail
we can read it and display it but we shouldnt be modify it

But what if we wanted to modify the global variable, then we would just return it for example 

"""

enemies = 1 

def increase_enemies(enemy):
    print(f"enemies inside a function {enemies}")
    return enemy + 1 

enemies = increase_enemies(enemies)

print(f"enemies outside of a function {enemies}")