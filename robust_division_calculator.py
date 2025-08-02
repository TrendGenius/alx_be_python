#!/usr/bin/env python3
# File: robust_division_calculator.py

def safe_divide(numerator_str, denominator_str):
    """
    Safely divides two numbers provided as strings, handling various exceptions.

    Args:
        numerator_str (str): The string representation of the numerator.
        denominator_str (str): The string representation of the denominator.

    Returns:
        str: A string containing either the successful division result or an error message.
    """
    try:
        # Convert the string arguments to floats.
        numerator = float(numerator_str)
        denominator = float(denominator_str)
        
        # Perform the division.
        # This will raise a ZeroDivisionError if the denominator is 0.
        result = numerator / denominator
        
        # If successful, return the result formatted to 2 decimal places.
        return f"Result: {result:.2f}"
    
    except ValueError:
        # This block is executed if `float()` fails to convert the input,
        # meaning the input was not a valid number.
        return "Error: Both inputs must be valid numbers."
        
    except ZeroDivisionError:
        # This block is executed if division by zero occurs.
        return "Error: Cannot divide by zero."

