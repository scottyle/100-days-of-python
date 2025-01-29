import random
import art

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(list_of_cards):
    """Calculates the score of a given list of cards"""
    if 11 in list_of_cards and 10 in list_of_cards and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards)>21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return sum(list_of_cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 21:
        return "You lose"
    elif u_score == 21:
        return "You win"
    elif c_score > 21:
        return "You win"
    elif u_score > 21:
        return "You lose"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = -1
    users_score = -1

    print(art.logo)
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        users_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, user score: {users_score}.")
        print(f"Computer first card: {computer_cards[0]}")

        if users_score == 0 or computer_score == 0 or users_score > 21 :
            is_game_over = True
        else:
            draw_another_card = input("Do you want to draw another card? [y/n]")
            if draw_another_card == "y":
                user_cards.append(deal_card())
                users_score = calculate_score(user_cards)
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, user score: {users_score}.")
    print(f"Computers cards: {computer_cards} Computers score: {computer_score}")
    print(compare(users_score, computer_score))


restart_game = input("Do you want to play a game? [y/n]")
while restart_game == "y":
    print("\n"*100)
    play_game()


