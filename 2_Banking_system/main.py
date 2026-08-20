# Banking System Specifications
# Goal

# Build a banking application that allows users to create accounts and perform basic banking operations.

# =========================
#       BANK SYSTEM
# =========================

# 1. Create Account
# 2. Deposit
# 3. Withdraw
# 4. Transfer
# 5. View Account
# 6. View All Accounts
# 7. Transaction History
# 8. Save Accounts
# 9. Load Accounts
# 10. Exit

# Choose an option:

accounts = {
    0: {"name": "Jose Perez","account_type": "savings", "currency": "dollars", "amount": 1000},
    1: {"name": "Clara Espacios","account_type": "savings", "currency": "dollars", "amount": 4500},
    2: {"name": "Lalo Pie","account_type": "savings", "currency": "dollars", "amount": 2000}
}

def create_account():
    account_number = len(accounts) + 1

    name = input("Add the owner's name: ")
    account_type = input("Select the account type: ")
    currency = input("Select the currency: ")
    amount = int(input("Select the amount you want to open this account: "))
    accounts[account_number] = {"name": name,"account_type": account_type, "currencys": currency}

def deposit():
    amount = int(input("Add the amount you wish to deposit: "))
    account_number = int(input("Select the account number you wish to deposit: "))

    try:
        accounts[account_number]['amount'] += amount
    except:
        print("Please only add numbers")



def withdraw():
    account_number = int(input("Select the account number you wish to withdraw: "))
    amount = int(input("Add the amount you wish to withdraw: "))
    
    try:
        new_amount = accounts[account_number]['amount'] - amount
        accounts[account_number]['amount'] = new_amount
        print(f"You have withdrawn {amount} and your new balance is {accounts[account_number]['amount']} ")
    except:
        print("Please only add numbers")

def transfer():
    pass

def view_account():
    pass

def view_all_accounts():
    pass

def transaction_history():
    pass

def saved_accounts():
    pass

def load_accounts():
    pass

withdraw()