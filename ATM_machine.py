class ATM_Machine:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self, input_pin):
        return self.pin == input_pin

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        print(f"Successfully deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Successfully withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance!")

    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = new_pin
            self.transaction_history.append("PIN changed successfully")
            print("PIN changed successfully.")
        else:
            print("Incorrect PIN!")

    def show_transaction_history(self):
        print("Transaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        for transaction in self.transaction_history:
            print(transaction)

def atm_menu():
    pin = int(input("Set your ATM PIN: "))
    atm = ATM_Machine(pin)
    
    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance Inquiry")
        print("2. Cash Deposit")
        print("3. Cash Withdrawal")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = int(input("Select an option: "))
        
        if choice == 1:
            print(f"Current balance: ${atm.check_balance()}")
        elif choice == 2:
            amount = float(input("Enter the amount: "))
            atm.deposit(amount)
        elif choice == 3:
            amount = float(input("Enter the amount: "))
            atm.withdraw(amount)
        elif choice == 4:
            old_pin = int(input("Enter your old PIN: "))
            new_pin = int(input("Enter your new PIN: "))
            atm.change_pin(old_pin, new_pin)
        elif choice == 5:
            atm.show_transaction_history()
        elif choice == 6:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    atm_menu()

