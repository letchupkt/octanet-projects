import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

# Initialize account details
balance = 1000  # Account balance
pin = "1234"  # Default PIN
transaction_history = []  # List to store transactions

# Function to verify PIN
def verify_pin():
    global pin
    attempts = 3
    while attempts > 0:
        entered_pin = simpledialog.askstring("PIN Verification", "Enter your PIN:", show='*')
        if entered_pin == pin:
            messagebox.showinfo("Success", "PIN verified.")
            return True
        else:
            attempts -= 1
            messagebox.showwarning("Error", f"Incorrect PIN. {attempts} attempts remaining.")
    messagebox.showerror("Blocked", "Too many incorrect attempts. Your card is blocked.")
    return False

# Function to check account balance
def check_balance():
    messagebox.showinfo("Account Balance", f"Your current balance is: ${balance:.2f}")

# Function to withdraw cash
def withdraw_cash():
    global balance
    amount = simpledialog.askfloat("Withdraw", "Enter the amount to withdraw:")
    if amount is None or amount <= 0:
        messagebox.showwarning("Invalid Input", "Amount must be positive.")
    elif amount > balance:
        messagebox.showwarning("Insufficient Funds", "Insufficient funds.")
    else:
        balance -= amount
        transaction_history.append(f"{datetime.now()}: Withdrew: ${amount:.2f}")
        messagebox.showinfo("Success", f"Withdrawal successful! New balance: ${balance:.2f}")

# Function to deposit cash
def deposit_cash():
    global balance
    amount = simpledialog.askfloat("Deposit", "Enter the amount to deposit:")
    if amount is None or amount <= 0:
        messagebox.showwarning("Invalid Input", "Amount must be positive.")
    else:
        balance += amount
        transaction_history.append(f"{datetime.now()}: Deposited: ${amount:.2f}")
        messagebox.showinfo("Success", f"Deposit successful! New balance: ${balance:.2f}")

# Function to update PIN
def update_pin():
    global pin
    new_pin = simpledialog.askstring("Change PIN", "Enter your new 4-digit PIN:", show='*')
    if new_pin and len(new_pin) == 4 and new_pin.isdigit():
        pin = new_pin
        messagebox.showinfo("Success", "Your PIN has been updated.")
    else:
        messagebox.showwarning("Invalid Input", "PIN must be a 4-digit number.")

# Function to view transaction history
def show_transaction_history():
    if transaction_history:
        history = "\n".join(transaction_history)
        messagebox.showinfo("Transaction History", history)
    else:
        messagebox.showinfo("Transaction History", "No transactions yet.")

# Create the main application window
app = tk.Tk()
app.title("ATM Simulation By lakshmikanthan")
app.geometry("400x500")
app.configure(bg='#d1d8e0')

# Frame for the ATM screen
frame = tk.Frame(app, bg='black', bd=10, relief=tk.RIDGE)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# ATM screen label
title_label = tk.Label(frame, text="Welcome to ATM Simulation", font=("Arial", 18, "bold"), fg='green', bg='black')
title_label.pack(pady=10)

# Verify PIN before accessing the ATM functions
if verify_pin():
    btn_font = ("Arial", 12, "bold")
    btn_bg = "#4CAF50"
    btn_fg = "white"
    
    tk.Button(frame, text="Check Balance", font=btn_font, bg=btn_bg, fg=btn_fg, command=check_balance, width=20).pack(pady=5)
    tk.Button(frame, text="Withdraw Cash", font=btn_font, bg=btn_bg, fg=btn_fg, command=withdraw_cash, width=20).pack(pady=5)
    tk.Button(frame, text="Deposit Cash", font=btn_font, bg=btn_bg, fg=btn_fg, command=deposit_cash, width=20).pack(pady=5)
    tk.Button(frame, text="Change PIN", font=btn_font, bg=btn_bg, fg=btn_fg, command=update_pin, width=20).pack(pady=5)
    tk.Button(frame, text="Transaction History", font=btn_font, bg=btn_bg, fg=btn_fg, command=show_transaction_history, width=20).pack(pady=5)
    tk.Button(frame, text="Exit", font=btn_font, bg="red", fg=btn_fg, command=app.quit, width=20).pack(pady=10)
else:
    app.destroy()

app.mainloop()
