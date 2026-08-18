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
    0: {"name": "Jose Perez","account_type": "savings", "currency": "dollars", "amount": "1000"},
    1: {"name": "Clara Espacios","account_type": "savings", "currency": "dollars", "amount": "1000"},
    2: {"name": "Lalo Pie","account_type": "savings", "currency": "dollars", "amount": "1000"}
}

def create_account():
    account_number = len(accounts) + 1

    name = input("Add the owner's name: ")
    account_type = input("Select the account type: ")
    currency = input("Select the currency: ")
    amount = input("Select the amount you want to open this account: ")
    accounts[account_number] = {"name": name,"account_type": account_type, "currencyss": currency}

def deposit():
    pass


def withdraw():
    pass

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

