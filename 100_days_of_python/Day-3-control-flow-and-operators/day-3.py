"""If else statement, a conditional statement that would mean that depending on a certain condition we would do either
A or B, it will look something like this
if condition:
    do this 
else: 
    do this
"""
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

#If this height is greater than 120 but not 120 if we wanted GE you would use this >= 
# if height > 120: 
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age >= 18:
#         print("Please pay $12.")
#     else:
#         print("Please pay $7.")
# else:
#     print("You cannot ride this rollercoaster")

#Introducing modulo, modulo works out the remainder 

#Check if the number is odd or even

# number = int(input("Input a number "))

# if number % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd")

"""Nested if statements and elif statements, which are used to represent a extra condition  
Note that only one of these conditions will be carried out 
if condition: 
    if another condition: 
        do this 
    else: 
        do this 
else: 
    do this 
"""
"""The above condition only checks the first if condition but what if you're in a situation which requires multiple conditions
even if the previous was already true. All of these conditions will be checked and if true be executed 
if condition1:
    do A
if condition2:
    do B
if condition3:
    do C
"""
bill = 0

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120: 
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7 
        print("Youth tickets are $7.")
    else:
        bill = 12 
        print("Adult tickets are $12.")
    wants_photos = input("Do you want a photo taken? Y/N ")
    if wants_photos == "Y":
        bill += 3

    print(f"Your final price is {bill}")
else:
    print("You cannot ride this rollercoaster")