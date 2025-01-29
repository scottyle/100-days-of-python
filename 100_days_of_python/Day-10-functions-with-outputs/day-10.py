#Functions 
"""
Functions that allow you to have an output once the function is completed 

def my_function():
    result = 3 * 2 
    return result (the output keyword)
output = result 

This means when we call this function later on and it runs it will go ahead and output this result and we can save it another variable 

"""

def format_name(f_name, l_name):
    #Convert these strings that get passed in
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())

    # print(f"Name: {formated_f_name} {formated_l_name}")
    #Instead of printing out this result we could also return it as well
    return (f"Name: {formated_f_name} {formated_l_name}")

formated_string = format_name("angela", "BOEYW")

print(formated_string)

"""What is the difference between a print statement and the output? Lets say we take the output of function_1 and we use 
it in function_2 how would we do that? """

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

# output = function_1("hello")
# print(output)
#We would do this

output = function_2(function_1("hello"))
print(output)


#Multiple return values
"""When a function encounters a line that has the word return on it, it knows that this line is the end of the function,
however you can have multiple return statements in one function, how does this work? 
"""
def format_name(f_name, l_name):
    #How can we get it to bypass the rest of the code if the user typed in a empty first name or last name? Multiple return values 
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"



print(format_name("AnGEla", "YU"))
