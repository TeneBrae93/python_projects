print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
name = input ("To get started, please provide your name: \n")
print(f"Hello {name}, let's see if you can find the treasure or die trying!\n")

# Set up the choice variables
choice1 = ""
choice2 = ""
choice3 = ""

# Story begins here
print("Your journey begins at Devil's Gulch as you look for the treasure left by the crazy train conductor.") 
choice1 = input("You have arrived at a crossroads in the path. Do you want to go right or left?\n")
if choice1 == "right" or choice1 == "Right":
    print("Game Over! You have been consumed by the Blue Dragon!")
elif choice1 == "left" or choice1 == "Left":
    print("You have come across a flooded path.") 
    choice2 = input("Do you swim or wait for the flood to go down?\n")
    if choice2 == "swim" or choice2 == "Swim":
        print("Game Over! You have drowned in the water. Next time wear a life jacket!") 
    elif choice2 == "wait" or choice2 == "Wait": 
        choice3 = input(f"Well {name} you are getting very close. You have arrived at three doors. Which one do you choose? Red? Blue? or Yellow?\n")
        if choice3 == "Red":
            print("Game Over! The red door exploded when you touched it and you are now dead. That sucks!")
        elif choice3 == "Blue":
            print("Game Over! The blue door shocked you when you touch it and your heart stopped. You are not dead. How shocking!")
        elif choice3 == "Yellow":
            print(f"Congratulations {name}, you have found the hidden treasure. Enjoy the loot!")

