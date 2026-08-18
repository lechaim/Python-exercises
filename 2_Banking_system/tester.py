
accounts = {
    0: {"name": "Jose Perez","account_type": "savings", "currency": "dollars", "amount": 1000},
    1: {"name": "Clara Espacios","account_type": "savings", "currency": "dollars", "amount": 4500},
    2: {"name": "Lalo Pie","account_type": "savings", "currency": "dollars", "amount": 2000}
}




try:
    print(accounts["a"])
except:
    print("Please only add numbers")

