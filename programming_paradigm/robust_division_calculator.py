#!/usr/bin/env python3
"""
This module contains a function to perform robust division, handling common errors.
"""

def safe_divide(numerator, denominator):
    """
    Performs division, handling ZeroDivisionError and ValueError.

    Args:
        numerator (str): The string representation of the numerator.
        denominator (str): The string representation of the denominator.

    Returns:
        str: A message indicating the result or the error encountered.
    """
    try:
        # Attempt to convert input strings to floating-point numbers
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero before performing the operation
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform the division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # This exception is caught if the conversion to float fails
        return "Error: Please enter numeric values only."
    except Exception as e:
        # A general catch-all for any other unexpected errors
        return f"An unexpected error occurred: {e}"