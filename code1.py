class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}. New Balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def transfer(self, target_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred: ${amount} to Account {target_account.account_number}")
        else:
            print("Transfer failed: Insufficient funds or invalid amount.")

    def display(self):
        print(f"Acc: {self.account_number} | Holder: {self.account_holder} | Balance: ${self.balance}")

#1} Create Accounts
acc1 = BankAccount("101", "Alice", 1000)
acc2 = BankAccount("102", "Bob", 500)

print("Initial Accounts:")
acc1.display()
acc2.display()

#2} Deposit
print("\n--- Testing Deposit ---")
acc1.deposit(200)

#3} Withdraw
print("\n--- Testing Withdraw ---")
acc1.withdraw(100)

#4} Transfer
print("\n--- Testing Transfer ---")
acc1.transfer(acc2, 300)

print("\nFinal Balances:")
acc1.display()
acc2.display()
