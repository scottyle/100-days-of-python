import art
import game_data as gd
import random

def higher_or_lower():
    """This data runs the game higher or lower"""
    #score variable to hold the current score
    score = 0
    game_over = False

    # Sets the variable to compare A
    compare_A = random.choice(gd.data)

    while not game_over:
        #print the art logo
        print(art.logo)

        # Set the variable to compare B
        compare_B = random.choice(gd.data)
        compare_A_name, compare_A_follower, compare_A_description, compare_A_country = parse_data(compare_A)
        compare_B_name, compare_B_follower, compare_B_description, compare_B_country = parse_data(compare_B)

        #Compare A pull a random data from the game_data, there are 50 list entries
        print(f"Compare A: {compare_A_name}, a {compare_A_description}, from {compare_A_country}.")
        print(art.vs)
        print(f"Compare B: {compare_B_name}, a {compare_B_description}, from {compare_B_country}.")

        #Comparision
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if compare_followers(user_input=user_guess, compare_A_follower = compare_A_follower, compare_B_follower = compare_B_follower):
            score += 1
            print(f"You're right! Current score {score}.")
            compare_A = compare_B
        else:
            print(f"Sorry, that's wrong. Final score was {score}.")
            game_over = True

    # Now we have to make this loop and continue if the user is always right.

def compare_followers(user_input, compare_A_follower, compare_B_follower):
    """This function returns True if the user guess correctly"""
    if user_input == "A" and compare_A_follower > compare_B_follower or user_input == "B" and compare_B_follower > compare_A_follower:
        return True

def parse_data(compare):
    """This function parses the data and returns it as a list """
    compare_name = compare["name"]
    compare_follower_count = compare["follower_count"]
    compare_description = compare["description"]
    compare_country = compare["country"]
    
    return compare_name, compare_follower_count, compare_description, compare_country

higher_or_lower()