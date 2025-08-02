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
    # The 'try' block is where we put the code that might cause an error.
    try:
        # We try to convert the string inputs from the command line
        # into numbers (floats). If the input is not a number, this will
        # cause a ValueError.
        num = float(numerator)
        den = float(denominator)

        # Now we try to perform the division. If 'den' is 0, this will
        # cause a ZeroDivisionError.
        result = num / den
        
        # If all of the above steps are successful, we return the result.
        # The project prompt specifies "The result of the division is 2.0".
        return f"The result of the division is {result}"
    
    # This 'except' block catches the specific error for division by zero.
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    # This 'except' block catches the specific error for non-numeric input.
    except ValueError:
        return "Error: Please enter numeric values only."
