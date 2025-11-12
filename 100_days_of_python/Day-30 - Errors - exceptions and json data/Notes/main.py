# FileNotFound 
# with open("a_file.txt") as file:
#     file.read()
# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     value = a_dict["key"]
# # except: #never use a bare except, this is because its going to ignore all errors, we want our exception to catch a specific situation 
# except FileNotFoundError:
#     file = open("a_file.txt","w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise TypeError("This is an error i made up.") #Raise our own exceptions, raise statement is used to manually trigger an exception 

# try:
#     file = open("data.txt") #FileNotFound Error 
# except FileNotFoundError:
#     print("File not found.")
# else:
#     print("File opened successfully!") #runs only if no error has occurred 
# finally:
#     print("This will run no matter what.")  # Always executes


#KeyError 
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

#IndexError 
# fruit_list = ["Apple","Banana","Pear"]
# fruits = fruit_list[3]

#TypeError 
# text = "abc"
# print(text + 5)

# """
# Handling exceptions 
# try -> trying to execute a line that may cause an exception 
# except -> block of code to be executed if there was an exception - do this if there was an exception 
# else -> do this if there were no exceptions 
# finally -> do this no matter what happens 
# """

#When would you want to raise a error. 

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should be over 3 meters.")

bmi = weight /height**2
print(bmi)
