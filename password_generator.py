import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Tyler's Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range(1, nr_letters + 1): 
    random_char = random.choice(letters)
    password += random_char

for symb in range (1, nr_symbols + 1):
    random_symb = random.choice(symbols)
    password += random_symb 

for number in range (1, nr_numbers + 1): 
    random_numb = random.choice(numbers)
    password += random_numb 

# Turns the password into a list 
password_split = [character for character in password]
# Shuffles the password to randomize it more
random.shuffle(password_split)
# Joins the split password back into a string
new_password = ''.join(password_split)

print(new_password)
