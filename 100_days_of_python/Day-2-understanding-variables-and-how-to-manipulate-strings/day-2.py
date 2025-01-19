"""len function to get the number of characters in a string, but what if we were to put a int into the function?
It would send back a TypeError. 
Basic data types 
1. Strings
2. Integers 
3. Floats 
4. Booleans
"""
print(len("Hello"))

"""The method of pulling out a particular element from a string is called subscripting for example """

#This prints the first element which is H 
print("Hello"[0])
#We can use negative indicies to get the ahold of the last element 
print("Hello"[-1])

#Integers are basically just whole numbers 
print(123 + 345)

#Large numbers, sometimes we put commas in the thousands but in python we can replace those commas by underscores 
#This just allows us to read the larger number much more easily 
print(123_456_789)

#How would we know the data type of a variable? We can use the type function, this is known as type checking 
print(type("Hello"))
print(type(231231))
print(type(21.23))
print(type(True))

"""What if we wanted to convert a data type, this is known as type casting/conversion"""
print(int(123) + int(456))
#For example these are the types of type casting we can do 
int()
bool()
str()
float()

print("Number of letters in your name: " + str(len(input("Enter your name: "))))

#Note division always leads to a float number but theres another division that you can use // 
#For example 
print(type(6/2))
#Note that this division will wipe out all of the decimals 
print(type(6//2))