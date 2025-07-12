# Task 5: Personal Finance Calculator
# Objective: Calculate monthly and projected annual savings based on user input.

# --- Part A: User Input for Financial Details ---
# 1. Prompt the user for their monthly income.
# The input() function gets text from the user.
# float() converts that text into a number that can have decimal places (like money).
monthly_income = float(input("Enter your monthly income: "))

# 2. Ask for their total monthly expenses.
monthly_expenses = float(input("Enter your total monthly expenses: "))

# --- Part B: Calculate Monthly Savings ---
# Monthly savings is simply income minus expenses.
monthly_savings = monthly_income - monthly_expenses

# --- Part C: Project Annual Savings ---
# 1. Define the annual interest rate as a decimal.
annual_interest_rate = 0.05  # Represents 5%

# 2. Calculate projected savings after one year.
# The formula is: (Monthly Savings * 12) + (Monthly Savings * 12 * Interest Rate)
# This calculates total savings for 12 months, then adds 5% interest on that total.
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# --- Part D: Output Results ---
# Display the calculated monthly savings.
# Using an f-string to include the variable value in the output text.
print(f"Your monthly savings are ${monthly_savings}.")

# Display the projected annual savings with interest.
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}.")
