############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random 
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
Author: Tyler Ramsbey
"""
                   
def blackjack(): 
    # Variables
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    print(logo)

    # Functions

    # Deal a single random card
    def deal_card(): 
        card = random.choice(cards)
        return card

    # Deal two random cards 
    def deal_two_cards(): 
        user_cards.append(deal_card()) 
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Calculate score based on the list of cards
    def calculate_score(list_of_cards):
        score = sum(list_of_cards)
        for card in list_of_cards:
            if card == 11 and score > 21: 
                list_of_cards.remove(11)
                list_of_cards.append(1)
                score = sum(list_of_cards) 
        if list_of_cards == [11, 10] or list_of_cards == [10, 11]: 
            return 0
        else:
            return score 

    # Initial check for winner and to finish the user's turn
    def calculate_winner():
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are: {user_cards}")
        # Per the rules, you only can see the computer's first card 
        print(f"The dealer's first card is: {computer_cards[0]}\n")
        if user_score == 0:
            should_continue = "You have a blackjack. You win and the game is over!"
            return should_continue 
        elif computer_score == 0:
            should_continue = "The dealer has a blackjack. You lose!"
            return should_continue
        elif user_score > 21: 
            should_continue = "You went over 21. You lose!"
            return should_continue 
        elif user_score <= 21:
            draw_card = input((f"Your current score is {user_score} do you want to draw another card? Type 'y' or 'n': "))
            if draw_card == 'y': 
                should_continue = "user" 
            elif draw_card == 'n':
                should_continue = "computer"
            return should_continue  

    # After the user is done, the computer/dealer will draw cards as long as their score is less than 17 per the rules
    def computers_turn():
        computer_score = calculate_score(computer_cards)
        if computer_score > 17:
            should_continue = f"The dealer's score is {computer_score}"
            return should_continue 
        while computer_score < 17: 
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            if computer_score < 17:
                should_continue = "computer" 
        if computer_score > 21: 
            should_continue = f"The dealer's score is {computer_score} and he went over 21. You win!"
            return should_continue 
        else:
            should_continue = computer_score  
            return should_continue 

    # Compare the scores to see who won
    def compare(user_score, computer_score): 
        if user_score == computer_score: 
            print(f"It's a draw! You both have a score of {user_score}.")
        elif user_score > computer_score: 
            print(f"You have a score of {user_score} and the dealer has a score of {computer_score} so you win!")
        else:
            print(f"You have a score of {user_score} and the dealer has a score of {computer_score} so you lose. Sorry!")
 
    # Main program -- calling various functions and variables 
    deal_two_cards() 
    should_continue = calculate_winner()  
    while should_continue == "user": 
        user_cards.append(deal_card())
        should_continue = calculate_winner() 
    while should_continue == "computer":
        should_continue = computers_turn() 
    if should_continue != calculate_score(computer_cards): 
        print(should_continue)
    computer_score = calculate_score(computer_cards)
    if should_continue == f"The dealer's score is {computer_score}" or should_continue == computer_score:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        compare(user_score, computer_score)
    start_over = input("Do you want to start another game? Type 'y' or 'n': ")
    # Recursion to start the game over 
    if start_over == "y": 
        blackjack()  
    else:
        print("Thank you for playing!")   
  
blackjack()
