# Initial welcome message to the tip calculator
print ("Welcome to the tip calculator.")

# Gets the total bill from the user
total_bill = input("What was the total bill? ")

# Takes the $ sign off so we can convert it to a floating point 
total_bill_int = float(total_bill[1:]) 

# Gets the tip percentage
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

# Converts the tip to a 0. value for calculation
tip_edit = '0.' + tip 
tip_percentage = float(tip_edit) 

# Gets the total bill for future calclation
bill_total = (total_bill_int * tip_percentage) + total_bill_int 

# Asks the user to input the total number of people to split the bill
total_people = int(input("How many people to split the bill? ")) 

# Calculates the total per person and rounds to 2 decimal places since it's a money value
total_per_person = round(bill_total / total_people, 2)

# Final statement to add the $ back to the print statement
print(f"Each person should pay: ${total_per_person}")
