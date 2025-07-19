# Task 2: Multiplication Table Generator
# Objective: Use a for loop to generate and print the multiplication table for a given number.

# --- Step 1: Prompt User for a Number ---
# Get a whole number from the user for the multiplication table.
number = int(input("Enter a number to see its multiplication table: "))

# --- Step 2: Generate and Print the Multiplication Table ---
# Use a for loop to iterate from 1 to 10 (inclusive).
# 'i' will take on values 1, 2, 3, ..., 10 in each loop.
for i in range(1, 11):
    # Calculate the product of the user's number and the current loop number.
    product = number * i
    # Print each line of the multiplication table in the specified format.
    print(f"{number} * {i} = {product}")
