'''
Coding Challenge: 
I had to create a "Silent Auction Program" that meets the following requirements:
-- Ask for name input 
-- Ask for bid price 
-- Add name and bid price into a dictionary as a key/value pair
-- Ask if there are other users who want to bid
---- If yes, clear the screen and repeat steps above
---- If no, find the highest bidder and declare them as the winner
'''

import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
# Declaring variables needed
bid_dict = {}
new_dict = {} 
other_bidders = ''
winner = ''

# Creating a function that asks for input for the "while" loop below 
def ask_bidders(): 
    if other_bidders == "yes":
        name = input("What's your name? ") 
        bid = input("What is your bid? $")

# Function which adds to the dictionary with the new values 
def bid_adder(name, bid):
    bid_dict[name] = bid  

# Main program starts here
print(logo) 
print("Welcome to the secret auction program.")
print("Author: Tyler Ramsbey\n")
name = input("What's your name? ") 
bid = input("What is your bid? $")
bid_adder(name, bid) 
winner_bet = bid_dict[name]
for name in bid_dict:
    winner = name  
other_bidders = input("Are there any other users who want to bid? Type 'yes' or 'no'.") 

# While loop so that if there are others it will clear screen and keep going through the loop
while other_bidders == "yes":
    multiple_people = "yes"  
    os.system('cls') 
    name = input("What's your name? ") 
    bid = input("What is your bid? $")
    bid_adder(name, bid) 
    other_bidders = input("Are there any other users who want to bid? Type 'yes' or 'no'. ")  

# This decides who the winner is 
for name in bid_dict:
    if int(bid_dict[name]) > int(winner_bet):
        winner_bet = int(bid_dict[name])
        winner = name 
 
# Final print statement!
print(f"The highest bidder is {winner} with a bid of ${winner_bet}. Congratulations!")
