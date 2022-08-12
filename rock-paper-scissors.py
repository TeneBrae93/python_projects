import random 
import time 

# Setting the artwork for the choices 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Set the user's choice based on input and set the opponent's choice based on random selection from a list
user_choice = input("Do you want to choose rock, paper, or scissors for your choice? Type R, P, or S: ")
possible = ["R", "P", "S"]
opponent_choice = (random.choice(possible))

# Print to the screen the choice of the user
if user_choice == "R": 
    print(f"You have chosen {rock}") 
elif user_choice == "S":
    print(f"You have chosen {scissors}")
else:
    print(f"You have chosen {paper}")

# Sleep to make it more realistic as opponent makes a choice 
print("Waiting for your opponent to choose...\n")
time.sleep(3)

# Print to the screen the choice of the opponent 
if opponent_choice == "R": 
    print(f"Your opponent has chosen {rock}") 
elif opponent_choice == "S":
    print(f"Your opponent has chosen {scissors}")
elif opponent_choice == "P":
    print(f"Your opponent has chosen {paper}")

# Results if user chooses rock
if user_choice == "R" and opponent_choice == "R": 
    print("You both chose rock so it's a draw!")
elif user_choice == "R" and opponent_choice == "S":
    print("You chose rock and your opponent chose scissors. Rock crushes scissors -- you win!")
elif user_choice == "R" and opponent_choice == "P": 
    print("You chose rock and your opponent chose paper. Paper covers rock. Your opponent wins!")

# Results if user chooses scissors 
if user_choice == "S" and opponent_choice == "S": 
    print("You both chose scissors so it's a draw!")
elif user_choice == "S" and opponent_choice == "R":
    print("You chose scissors and your opponent chose rock. Rock crushes scissors -- you lose!")
elif user_choice == "S" and opponent_choice == "P":
    print("You chose scissors and your opponent chose paper. Scissors cuts paper. You win!")

# Results if user chooses paper 
if user_choice == "P" and opponent_choice == "P": 
    print("You both chose paper so it's a draw!")
elif user_choice == "P" and opponent_choice == "R":
    print("You chose paper and your opponent chose rock. Paper covers rock -- you win!")
elif user_choice == "P" and opponent_choice == "S": 
    print("You chose paper and your opponent chose scissors. Scissor cuts paper. You lose!")
