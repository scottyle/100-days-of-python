print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_decision = input("You're at a cross road. Where do you want to go? left or right ").lower()

if first_decision == "left":
    second_decision = input("You're come to a lake. There is a island in the middle of the lake. Type 'wait' to wait for a bit.\nType 'swim' to swim across. ").lower()
    if second_decision == "wait":
        third_decision = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose? ").lower()
        if third_decision == "red":
            print("Burned by fire. Game over")
        elif third_decision == "blue":
            print("Eaten by beasts. Game over.")
        elif third_decision == "yellow":
            print("You Win!")
        else: 
            print("Incorrect. Game over.")
    elif second_decision == "swim":
        print("You get attacked by an angry trout. Game over.")
elif first_decision == "right":
    print("You fell into a hole. Game over.")
else:
    print("Please select a valid input.")