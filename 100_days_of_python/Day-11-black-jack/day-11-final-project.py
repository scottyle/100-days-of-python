import art
import random

#Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

players_cards = []
players_score = 0
computers_cards = []
computers_score = 0
game_over = False

def check_hand_value(users_cards):
    card_sum = sum(users_cards)
    if card_sum == 21:
        return 0
    else:
        return card_sum

def draw_new_card(users_cards):
    users_cards.append(random.choice(cards))
    return users_cards


while not game_over:
    play_game = input("Do you want to play Blackjack? Type 'y' or 'n': ")

    #Initialize the game
    if play_game == "y":
        print(art.logo)

        #Deal two cards to the user and computer
        for _ in range(2):
            players_cards.append(random.choice(cards))
            computers_cards.append(random.choice(cards))

        #Show the users their cards and the dealers first card but check if either one hit blackjack already and save sums of cards in a variable
        players_score = check_hand_value(players_cards)
        computers_score = check_hand_value(computers_cards)

        print(f"Your cards: {players_cards}, current score: {players_score}")
        print(f"Computer's first card: {computers_cards[0]}")

        #This checks if either the players score or computers score is 21 and ends if it is
        if players_score == 0 or computers_score == 0:
            print(f"Your final hand: {players_cards}, final score: {players_score}")
            print(f"Computer's final hand: {computers_cards}, final score: {computers_score}")
            #We have to see which person won
            if players_score == 0:
                print("Win with a blackjack!")
            elif computers_score == 0:
                print("Lose!")
            game_over = True

        #If no one has won yet, this checks if the user wants to draw another card
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_card == "y":
            #Draw a new card for the player
            players_cards = draw_new_card(players_cards)
            #I have to call the players_score check sum function again to check the score.
            players_score = check_hand_value(players_cards)

            print(f"Your cards: {players_cards}, current score: {players_score}")
            print(f"Computer's first card: {computers_cards[0]}")

            #We need to check if the users hand is above 21 or equal to 21, then the computer must draw cards to see if they win

            if players_score > 21:
                print(f"Your final hand: {players_cards}, final score: {players_score}")
                print("You went over. You lose")
                game_over = True
            elif players_score == 0:
                #If you hit 21 then the computer must draw cards to check if the win or lose.
                computers_cards = draw_new_card(computers_cards)
                #Check the sum for the computer
                computers_score = check_hand_value(computers_cards)
                if computers_score < players_score:
                    print("You win")
                elif computers_score == players_score:
                    print("Draw")

    elif play_game == "n":
        print("Goodbye")
        game_over = True

    else:
        print("Invalid input")