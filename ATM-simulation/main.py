# Import the time module for simulating delays
import time 







# Initialize account details
balance = 1000  # Account balance
pin = "1234"  # Default PIN
transaction_history = []  # List to store transactions





# Function to display ATM menu
def show_menu():
    print("\nATM Menu:")
    print("1. Check Account Balance")
    print("2. Withdraw Cash")
    print("3. Deposit Cash")
    print("4. Change PIN")
    print("5. View Transaction History")
    print("6. Exit")




# Function to verify the entered PIN
def verify_pin():
    print("Please insert your card...")
    time.sleep(3)  # Simulate card insertion delay
    
    entered_pin = input("Enter your PIN: ")
    if entered_pin != pin:
        print("Incorrect PIN.")
        return False
    return True




# Function to check account balance
def check_balance():
    print(f"Your current balance is: ${balance}")





# Function to withdraw cash
def withdraw_cash():
    amount = float(input("Enter the amount you wish to withdraw: $"))
    
    global balance
    if amount <= balance:
        balance -= amount
        transaction_history.append(f"Withdrew: ${amount}")
        print(f"Withdrawal successful! Your new balance is: ${balance}")
    else:
        print("Insufficient funds.")




# Function to deposit cash
def deposit_cash():
    amount = float(input("Enter the amount you wish to deposit: $"))
    
    global balance
    balance += amount
    transaction_history.append(f"Deposited: ${amount}")
    print(f"Deposit successful! Your new balance is: ${balance}")




# Function to change the account PIN
def update_pin():
    new_pin = input("Enter your new PIN: ")
    global pin
    pin = new_pin
    print("Your PIN has been updated.")



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
    while True:
        if verify_pin():  # Ask for PIN before showing menu
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
                break
            else:
                print("Invalid option.")
        else:
            continue  # Retry PIN if incorrect

# Start the ATM simulation
start_atm()
