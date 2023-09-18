"""
Utilities for the ATM program.
"""


def check_balance(balance):
    print("[ATM] Your balance is $" + str(balance) + ".")


def withdraw(balance):
    amount = float(input("[ATM] How much would you like to withdraw? $"))
    if amount > balance:
        print("[ATM] You do not have enough money to withdraw that amount.")
        return balance
    else:
        balance -= amount
        print("[ATM] You have withdrawn $" + str(amount) + ".")
        return balance


def deposit(balance):
    amount = float(input("[ATM] How much would you like to deposit? $"))
    balance += amount
    print("[ATM] You have deposited $" + str(amount) + ".")
    return balance
