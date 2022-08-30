# Art work 
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88
Author: Tyler Ramsbey                          
"""


# Variables 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encrypted_message = []
decrypted_message = []

# Ask for user input 
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Caesar Function -- encodes and decodes based on user input 
def caesar(text, shift, direction):
    if direction == "encode":
        for letter in text:
            try:
                current_position = alphabet.index(letter)
                new_position = current_position + shift
                if new_position > 26:
                    new_position -= 26   
                encrypted_message.append(alphabet[new_position])
                encrypted_message_joined = ''.join(encrypted_message)
            except:
                encrypted_message.append(letter)
        print(f"The encrypted message is {encrypted_message_joined}")
    else:
        for letter in text:
            try:
                current_position = alphabet.index(letter)
                new_position = current_position - shift 
                decrypted_message.append(alphabet[new_position])
                decrypted_message_joined = ''.join(decrypted_message)
            except:
                decrypted_message.append(letter)
        print(f"The decoded message is {decrypted_message_joined}")

caesar(text, shift, direction)
