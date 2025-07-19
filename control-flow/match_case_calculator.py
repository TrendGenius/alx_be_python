# Task 1: Simple Calculator with Match Case
# Objective: Use Match Case statements for handling multiple operations.

# --- Step 1: Prompt for User Input ---
# Get the first number from the user. Convert it to a float to handle decimals.
num1 = float(input("Enter the first number: "))
# Get the second number from the user.
num2 = float(input("Enter the second number: "))
# Get the desired operation from the user.
operation = input("Choose the operation (+, -, *, /): ")

# --- Step 2: Perform the Calculation Using Match Case ---
# The 'match' statement checks the value of the 'operation' variable.
# Each 'case' is a possible value for 'operation'.
match operation:
    case "+":
        # If operation is "+", perform addition.
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        # If operation is "-", perform subtraction.
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        # If operation is "*", perform multiplication.
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        # If operation is "/", first check for division by zero.
        if num2 == 0:
            # If num2 is 0, print an error message.
            print("Cannot divide by zero.")
        else:
            # Otherwise, perform division.
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        # The underscore '_' acts as a wildcard or default case.
        # If 'operation' doesn't match any of the above cases, print an error.
        print("Invalid operation. Please choose from +, -, *, /.")
