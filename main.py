#!/usr/bin/env python3
# File: main.py

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command line arguments and call the safe_divide function.
    """
    # The 'sys.argv' list contains all command-line arguments.
    # sys.argv[0] is always the script name itself.
    # We need 3 items in total: the script name, the numerator, and the denominator.
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        # We exit the program with an error code of 1, indicating a failure.
        sys.exit(1)

    # We retrieve the arguments from the list. They are always strings.
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # We call our 'safe_divide' function with the arguments.
    # The function returns a string with either the result or an error message.
    result = safe_divide(numerator, denominator)
    
    # We print the string returned by our function.
    print(result)

if __name__ == "__main__":
    main()