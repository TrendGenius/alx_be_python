# Task 4: User Input Age Calculator
# Objective: Ask the user for their current age and calculate their age in a future year.

# Prompt the user to input their current age
# The input() function displays the message and waits for the user to type.
# int() converts the text the user types into a whole number, so we can do math with it.
current_age = int(input("How old are you? "))

# Define how many years to add (2050 - 2023 = 27)
years_to_add = 27

# Calculate the user's age in 2050
future_age = current_age + years_to_add

# Print the user's age in 2050 in the specified format
print(f"In 2050, you will be {future_age} years old.")