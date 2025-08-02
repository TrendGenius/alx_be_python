#!/usr/bin/env python
# programming_paradigm/bank_account.py
# This script defines the BankAccount class.

class BankAccount:
    """
    A class to represent a simple bank account.

    This class demonstrates basic OOP principles like encapsulation,
    with methods to deposit, withdraw, and display the account balance.
    """

    def __init__(self, initial_balance=0):
        """
        The constructor method to initialize a new BankAccount object.

        It sets the starting balance for the account. The '__init__' method
        is automatically called when a new object is created from the class.

        Args:
            initial_balance (float, optional): The starting amount for the
                                                account. Defaults to 0.
        """
        # 'self.account_balance' is an attribute (a variable) that belongs
        # to this specific instance of the BankAccount.
        # It stores the current balance.
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to be deposited.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            # You can add more robust error handling here, but for this task,
            # we just ensure the amount is positive.
            pass

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        Withdrawal is only successful if the account has sufficient funds.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        # Check if the account has enough money to withdraw
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True  # Withdrawal was successful
        else:
            return False # Insufficient funds or invalid amount

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        # This method accesses the 'account_balance' attribute of the
        # current object instance ('self').
        print(f"Current Balance: ${self.account_balance}")
