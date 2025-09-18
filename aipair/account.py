# Create Account class with the following attributes
# acno, ahname, balance and methods like - __init__, deposit, withdraw, get_balance

class Account:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.current_balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited: {amount}. New balance: {self.current_balance}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.current_balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.current_balance


