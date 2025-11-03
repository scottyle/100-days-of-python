#Instead of using a close statement everytime you open a file in Python many developers use the with open syntax
#For example, this way we do not need to add the close syntax and remember to close the file everytime 
# with open("my_file.txt") as file:

#     contents = file.read()
#     print(contents)
#Why do we have to close up a file? When python opens up a file it takes some of its resources and we dont know when
#its going to let go of those resources 
# file.close()

#What if instead of reading the file we want to write to it?

with open("/my_file.txt",mode="a") as file:
    file.write("\nNew text.")

#One important thing when you set the mode to "w" and that file does not exist then python is going to generate that file for you 

"""Understanding file paths 
At the very root of files is basically the origin 
Absolute files paths always start off relative to the root 
Relative file path the path that is relative to the file you're calling 
The current directory you're in is called the working directory

What if we wanted to change this path that is relative to our current main.py 
"""