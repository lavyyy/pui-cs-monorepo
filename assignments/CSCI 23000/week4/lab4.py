"""
Name: Cayden Young
Course: CSCI 23000
Assignment: Lab 4
Date: 9/17/2023
"""

from lab4_utils import check_balance, withdraw, deposit


def main():
    # Inital balance
    balance = 1000.00

    print("[ATM] Welcome to the ATM!")
    print(" 1. Check Balance")
    print(" 2. Withdraw")
    print(" 3. Deposit")
    print(" 4. Quit")
    print("")

    # Get user input
    choice = int(input("Please make your selection: "))

    # Handle user input
    if choice == 1:
        check_balance(balance)
    elif choice == 2:
        balance = withdraw(balance)
    elif choice == 3:
        balance = deposit(balance)
    elif choice == 4:
        return
    else:
        print("[ATM] Invalid choice. Please try again.")
        main()


if __name__ == "__main__":
    main()
