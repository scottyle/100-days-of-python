#Loops
"""For loop, by using this for loop we can go through each item in the list and perform some action with each item
for item in list_of_items:
    #Do something to each item
Loops allows us to execute the same line of the code multuple times"""

# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

#This is equalvalent to using the sum() function
# student_scores = [150, 142, 185 , 120, 171, 184,149,24,59,68,199,78,65,89]
# total_score = 0 
# # for score in student_scores:
# #     print(total_score)
# #     total_score += score 

# #Lets replicate the max function 
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(highest_score)

"""For loops and the range() function 
Sometimes we're not always going to use loops for lists, the range function is really good when we want to generate a 
range of numbers to loop through 

for number in range (a,b)L
    print(number)

note that the range function doesn't do anything on its own 
"""
total_sum = 0 

for number in range(1,101):
    total_sum = number + total_sum

print(total_sum)