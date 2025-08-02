#!/usr/bin/env python3
# programming_paradigm/main-0.py
# This script demonstrates the usage of the BankAccount class by handling
# command-line arguments to perform different operations.

# Import the BankAccount class from the bank_account.py file.
from bank_account import BankAccount
# Import the sys module to access command-line arguments.
import sys

def main():
    """
    Main function to run the bank account operations based on command-line arguments.
    """
    # 1. Create a new BankAccount object with an initial balance.
    #    Let's start with a balance of $100 to better demonstrate withdrawals.
    my_account = BankAccount(initial_balance=100.00)
    
    # 2. Display the initial balance before any operations.
    print("Initial Balance:")
    my_account.display_balance()
    
    # 3. Check if a command-line argument was provided.
    #    sys.argv[0] is always the script name itself, so we check for an index of 1.
    if len(sys.argv) > 1:
        # The command should be in the format "action:amount"
        try:
            command, amount_str = sys.argv[1].split(':')
            amount = float(amount_str)
            
            # 4. Process the command.
            if command == 'deposit':
                print(f"\nDepositing ${amount:.2f}...")
                my_account.deposit(amount)
            elif command == 'withdraw':
                print(f"\nAttempting to withdraw ${amount:.2f}...")
                success = my_account.withdraw(amount)
                if not success:
                    print("Withdrawal failed: Insufficient funds.")
            else:
                print(f"\nInvalid command: '{command}'. Please use 'deposit:amount' or 'withdraw:amount'.")

        except (ValueError, IndexError):
            # This handles cases where the argument format is incorrect, e.g., "withdraw" or "withdraw:abc"
            print(f"\nInvalid argument format. Please use 'deposit:amount' or 'withdraw:amount'.")
    else:
        print("\nNo operation specified. Use 'deposit:amount' or 'withdraw:amount' to perform an action.")

    # 5. Display the final balance after the operation (or lack thereof).
    print("\nFinal Balance:")
    my_account.display_balance()

# Run the main function.
if __name__ == "__main__":
    main()
