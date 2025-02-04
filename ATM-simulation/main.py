# Importing necessary library for time simulation
import time 

# Initializing account data
balance = 1000  # Initial balance in the account
pin = "1234"  # Default PIN for the account
transaction_history = []  # List to store all transaction records (withdrawals and deposits)

def display_menu():
    
    #Displays the available ATM menu options to the user.
    
    print("\nATM Menu:")
    print("1. Account Balance Inquiry")  # Option for checking account balance
    print("2. Cash Withdrawal")          # Option for withdrawing cash
    print("3. Cash Deposit")             # Option for depositing cash
    print("4. Change PIN")               # Option for changing the account PIN
    print("5. Transaction History")      # Option to view past transactions
    print("6. Exit")                     # Option to exit the ATM simulation

def check_pin():

    print("Insert Your Card")  
    time.sleep(5)  # Simulate card insertion time of 5 seconds
    
    # Ask the user to enter their PIN for authentication
    entered_pin = input("Enter your PIN: ")
    
    # If the entered PIN is incorrect, print an error and return False
    if entered_pin != pin:
        print("Incorrect PIN. Try again.")
        return False
    return True  # If the PIN is correct, return True to allow access

def account_balance_inquiry():
    
    #Displays the current balance of the user's account.
    
    print(f"Your account balance is: ${balance}")

def cash_withdrawal():
    
    # Ask the user to enter the withdrawal amount
    amount = float(input("Enter the amount you wish to withdraw: $"))
    
    global balance  # Use the global balance variable to update it
    
    # Check if the user has enough balance for the withdrawal
    if amount <= balance:
        balance -= amount  # Deduct the amount from the balance
        transaction_history.append(f"Withdrew: ${amount}")  # Add the transaction to the history
        print(f"Withdrawal successful. Your new balance is: ${balance}")
    else:
        print("Insufficient balance.")  # If balance is insufficient, show an error message

def cash_deposit():
    
    # Ask the user to enter the deposit amount
    amount = float(input("Enter the amount you wish to deposit: $"))
    
    global balance  # Use the global balance variable to update it
    
    balance += amount  # Add the deposit amount to the balance
    transaction_history.append(f"Deposited: ${amount}")  # Add the transaction to the history
    print(f"Deposit successful. Your new balance is: ${balance}")

def change_pin():
    
    # Ask the user to input a new PIN
    new_pin = input("Enter your new PIN: ")
    
    global pin  # Use the global pin variable to update it
    pin = new_pin  # Update the account PIN with the new PIN
    print("PIN changed successfully.")  # Notify the user that the PIN has been updated

def transaction_history_inquiry():
    
    if transaction_history:
        print("\nTransaction History:")
        for transaction in transaction_history:
            print(transaction)  # Print each transaction in the history
    else:
        print("No transactions yet.")  # If no transactions, inform the user

def run_atm():
    
    while True:
        # Ask for the PIN before showing the menu options
        if check_pin():
            # If the PIN is correct, display the ATM menu
            display_menu()
            choice = input("Choose an option (1-6): ")

            # Execute the corresponding function based on the user's choice
            if choice == '1':
                account_balance_inquiry()  # Option 1: Check balance
            elif choice == '2':
                cash_withdrawal()  # Option 2: Withdraw cash
            elif choice == '3':
                cash_deposit()  # Option 3: Deposit cash
            elif choice == '4':
                change_pin()  # Option 4: Change PIN
            elif choice == '5':
                transaction_history_inquiry()  # Option 5: View transaction history
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")  # Exit option
                break  # Exit the ATM simulation
            else:
                print("Invalid option. Please choose a valid option (1-6).")  # Invalid option error
        else:
            continue  # Retry PIN if the entered PIN is incorrect

# Running the ATM simulation
run_atm()
