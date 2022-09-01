# This was a coding challenge to create a calculator with the following features:
# -- Uses a dictionary to calculate the sums of numbers entered by the user based on operation symbol and functions 
# -- Continues to perform operations on the number until the user stops it 
# -- Uses recursion to start a new calculation at the user's requests 

import os

logo = """
 _____________________
|  _________________  |
| |   Calculator!   | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

Author: Tyler Ramsbey
"""

# Mathematic Functions
def add(n1, n2):
    return n1 + n2 

def subtract(n1, n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2 

def divide(n1, n2):
    return n1 / n2 

# Math Dictionary 
operations = {
    "+": add, 
    "-": subtract,
    "*": multiply, 
    "/": divide, 
} 


def calculator():
    print(logo) 
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator) 
    should_continue = True 

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2) 

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == "y": 
            num1 = answer
        else:
            should_continue = False
            os.system('cls') 
            calculator() 

calculator() 
