#Guess the number game
import random
import art

def guess_game(answer,difficulty):
    """This function runs the game for the user"""
    while difficulty > 0:
        print(f"You have {difficulty} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        difficulty -= 1
        if user_guess == answer:
            print(f"You got it! The answer was {answer}")
            break
        elif user_guess > answer:
            print("Too high.")
            print("Guess again.")
        elif user_guess < answer:
            print("Too low.")
            print("Guess again.")
        else:
            print("Incorrect input. -1 life.")
        if difficulty == 0:
            print(f"Game Over. The correct number was {answer}")



print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#Generate the random number between 1-100
correct_number = random.randint(1, 100)
print(f"Psst, the correct answer is {correct_number}")

#Let the user choose hard or easy
easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

#Hard lives = 5 and Easy lives = 10
HARD_LIVES = 5
EASY_LIVES = 10

#Depending if the user chooses easy or hard call the correct function

if easy_or_hard == "easy":
    guess_game(answer = correct_number, difficulty= EASY_LIVES)
elif easy_or_hard == "hard":
    guess_game(answer = correct_number, difficulty= HARD_LIVES)
else:
    print("Incorrect input.")