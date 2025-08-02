#!/usr/bin/env python3
# programming_paradigm/main-0.py
# This script handles command line interaction for the BankAccount class.

import sys
from bank_account import BankAccount

def main():
    """
    Main function to parse command line arguments and interact with BankAccount.
    """
    # Create a new BankAccount instance with an initial balance of $100 for testing.
    account = BankAccount(100)
    
    # Check if a command was provided.
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the first command line argument into command and parameters.
    try:
        command, *params = sys.argv[1].split(':')
    except ValueError:
        print("Invalid command format. Use <command>:<amount>.")
        sys.exit(1)

    # Try to convert the amount parameter to a float.
    amount = None
    if params:
        try:
            amount = float(params[0])
        except (ValueError, IndexError):
            print("Invalid amount. Please provide a numeric value.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()
