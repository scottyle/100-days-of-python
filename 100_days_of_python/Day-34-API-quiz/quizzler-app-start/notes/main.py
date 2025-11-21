"""
Dynamic typing means that variables in python are not bound to a specific type at declaration, 
this means that the variables in python can change etc. 

Type Casting is the method to convert the Python variable datatype 
into a certain data type in order to perform the required operation by users.

To make programs less error prone we can declare a type for a specific input for example police_check
function we can declare that the age variable has to be a int 
"""
age:int
age = "12" 

#the -> states the output of the function 
def police_check(age:int)->bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False 
    return can_drive

print(police_check(12))

if police_check("twelve"):
    print("you may pass")
else:
    print("Pay a fine.")