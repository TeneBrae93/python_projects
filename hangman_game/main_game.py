import random
import hangman_words
import hangman_art

# Setting initial variables for the game 
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
guess_history = [] 
end_of_game = False
lives = 6

# Importing the logo from hangman_art module 
print(hangman_art.logo) 

# Testing code -- comment this out to play the actual game 
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Start the "while" loop based on whether or not it's the "end_of_game"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Check to see if user already entered the letter and let me know if they have 
    for guesses in guess_history:
        if guesses == guess:
            print(f"You already guessed {guess}!")
    guess_history.append(guess) 

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Your guess of {guess} is not in the word. Try again!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the "stages" from the hangman_art module 
    print(hangman_art.stages[lives]) 

