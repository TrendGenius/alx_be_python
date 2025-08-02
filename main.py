#!/usr/bin/env python3
# File: main.py

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command line arguments and call the safe_divide function.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()