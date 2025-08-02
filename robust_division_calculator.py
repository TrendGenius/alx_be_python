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
        num = float(numerator)
        den = float(denominator)

        result = num / den
        
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
