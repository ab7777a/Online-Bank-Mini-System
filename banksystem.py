import json
import os
from datetime import datetime

DATA_FILE = "bank_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log(msg):
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def create_account(accounts):
    acc_no = input("Account Number: ").strip()
    if acc_no in accounts:
        log("ERROR: Account already exists!")
        return
    accounts[acc_no] = {
        "holder": input("Holder Name: ").strip(),
        "balance": float(input("Initial Balance: ")),
        "kyc": input("KYC Verified? (y/n): ").lower() == 'y'
    }
    save_data(accounts)
    log(f"Account {acc_no} created successfully!")

def show_accounts(accounts):
    if not accounts:
        log("No accounts found.")
        return
    print("\n" + "="*60)
    print(f"{'Account':<15} {'Holder':<15} {'Balance':<12} {'KYC'}")
    print("="*60)
    for acc, data in accounts.items():
        kyc = "✓ YES" if data['kyc'] else "✗ NO"
        print(f"{acc:<15} {data['holder']:<15} ${data['balance']:<11.2f} {kyc}")
    print("="*60)

def deposit(accounts):
    acc = input("Account Number: ").strip()
    if acc not in accounts:
        log("ERROR: Account not found!")
        return
    amount = float(input("Amount to deposit: "))
    accounts[acc]['balance'] += amount
    save_data(accounts)
    log(f"Deposited ${amount:.2f}. New balance: ${accounts[acc]['balance']:.2f}")

def withdraw(accounts):
    acc = input("Account Number: ").strip()
    if acc not in accounts:
        log("ERROR: Account not found!")
        return
    amount = float(input("Amount to withdraw: "))
    if accounts[acc]['balance'] < amount:
        log("ERROR: Insufficient balance!")
        return
    accounts[acc]['balance'] -= amount
    save_data(accounts)
    log(f"Withdrew ${amount:.2f}. New balance: ${accounts[acc]['balance']:.2f}")

def transfer(accounts):
    sender = input("Sender Account: ").strip()
    receiver = input("Receiver Account: ").strip()
    
    if sender not in accounts or receiver not in accounts:
        log("ERROR: One or both accounts not found!")
        return
    if sender == receiver:
        log("ERROR: Cannot transfer to same account!")
        return
    if not accounts[sender]['kyc']:
        log("ERROR: Sender is not KYC verified!")
        return
    
    amount = float(input("Amount to transfer: "))
    if accounts[sender]['balance'] < amount:
        log(f"ERROR: Insufficient balance! (Available: ${accounts[sender]['balance']:.2f})")
        return
    
    accounts[sender]['balance'] -= amount
    accounts[receiver]['balance'] += amount
    save_data(accounts)
    log(f"Transferred ${amount:.2f} from {sender} to {receiver}")

def main():
    accounts = load_data()
    
    while True:
        print("\n" + "="*40)
        print("   SECURE BANK MINI SYSTEM")
        print("="*40)
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer Money")
        print("6. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            show_accounts(accounts)
        elif choice == '3':
            deposit(accounts)
        elif choice == '4':
            withdraw(accounts)
        elif choice == '5':
            transfer(accounts)
        elif choice == '6':
            log("Goodbye!")
            break
        else:
            log("Invalid option!")

if __name__ == "__main__":
    main()