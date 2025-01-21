#Rock paper and scissors 
import random
import rock_paper_or_scissors

user_choice = int(input(("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")))
computer_choice = random.randint(0,2)

#User choices 
if user_choice == 0:
    print(rock_paper_or_scissors.rock)
elif user_choice == 1:
    print(rock_paper_or_scissors.paper)
elif user_choice == 2:
    print(rock_paper_or_scissors.scissors)
else:
    print("Invalid input")
    
print("Computer chose: ")

#Computer choices 

if computer_choice == 0:
    print(rock_paper_or_scissors.rock)
elif computer_choice == 1:
    print(rock_paper_or_scissors.paper)
elif computer_choice == 2:
    print(rock_paper_or_scissors.scissors)

if user_choice == computer_choice:
    print("Draw")
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
    print("You lose")
elif ((user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1)):
    print("You win")