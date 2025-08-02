#!/usr/bin/env python3
# File: robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling for division by zero and
    non-numeric inputs.

    Args:
        numerator (str): The string value for the numerator.
        denominator (str): The string value for the denominator.

    Returns:
        str: A message indicating the result of the division or an error.
    """
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Perform the division
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        # Catch and handle division by zero
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Catch and handle non-numeric input
        return "Error: Please enter numeric values only."


# Example usage (for testing, not part of the command line interaction)
if __name__ == "__main__":
    print(safe_divide("10", "5"))   # Normal division
    print(safe_divide("10", "0"))   # Division by zero
    print(safe_divide("ten", "5"))  # Invalid input
    print(safe_divide("10", "five")) # Another invalid input
