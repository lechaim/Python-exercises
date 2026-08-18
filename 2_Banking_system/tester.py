
accounts = {
    0: {"name": "Jose Perez","account_type": "savings", "currency": "dollars"},
    1: {"name": "Clara Espacios","account_type": "savings", "currency": "dollars"},
    2: {"name": "Lalo Pie","account_type": "savings", "currency": "dollars"}
}


account_number = len(accounts) + 1
name = input("Add the owner's name: ")
account_type = input("Select the account type: ")
currency = input("Select the currency: ")
accounts[account_number] = {"name": name,"account_type": account_type, "currencyss": currency}

print(accounts)




