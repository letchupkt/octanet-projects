# Import the time module for simulating delays
import time
from datetime import datetime

# Initialize account details
balance = 1000  # Account balance
pin = "1234"  # Default PIN
transaction_history = []  # List to store transactions

# Function to display ATM menu
def show_menu():
    print("\n   ATM Menu:")
    print("         1. Check Account Balance")
    print("         2. Withdraw Cash")
    print("         3. Deposit Cash")
    print("         4. Change PIN")
    print("         5. View Transaction History")
    print("         6. Exit")

# Function to verify the entered PIN
def verify_pin():
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == pin:
            print("PIN verified.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. {attempts} attempts remaining.")
    print("Too many incorrect attempts. Your card is blocked.")
    return False

# Function to check account balance
def check_balance():
    print(f"Your current balance is: ${balance:.2f}")

# Function to withdraw cash
def withdraw_cash():
    global balance
    try:
        amount = float(input("Enter the amount you wish to withdraw: $"))
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            transaction_history.append(f"{datetime.now()}: Withdrew: ${amount:.2f}")
            print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to deposit cash
def deposit_cash():
    global balance
    try:
        amount = float(input("Enter the amount you wish to deposit: $"))
        if amount <= 0:
            print("Amount must be positive.")
        else:
            balance += amount
            transaction_history.append(f"{datetime.now()}: Deposited: ${amount:.2f}")
            print(f"Deposit successful! Your new balance is: ${balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to change the account PIN
def update_pin():
    global pin
    new_pin = input("Enter your new PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        pin = new_pin
        print("Your PIN has been updated.")
    else:
        print("PIN must be a 4-digit number.")

# Function to view transaction history
def show_transaction_history():
    if transaction_history:
        print("\nTransaction History:")
        for transaction in transaction_history:
            print(transaction)
    else:
        print("No transactions yet.")

# Main function to run the ATM program
def start_atm():
    print("<=============ATM SIMULATION=============>")
    while True:
        if verify_pin():  # Ask for PIN before showing menu
            while True:
                show_menu()  # Display menu options
                choice = input("Choose an option (1-6): ")

                if choice == '1':
                    check_balance()
                elif choice == '2':
                    withdraw_cash()
                elif choice == '3':
                    deposit_cash()
                elif choice == '4':
                    update_pin()
                elif choice == '5':
                    show_transaction_history()
                elif choice == '6':
                    print("Thank you for using the ATM. Goodbye!")
                    return
                else:
                    print("Invalid option. Please choose a number between 1 and 6.")
        else:
            break  # Exit if PIN verification fails

# Start the ATM simulation
start_atm()
