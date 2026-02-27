accounts = {
    "1001": {"name": "Alice", "pin": "1234", "balance": 5000},
    "1002": {"name": "Bob", "pin": "5678", "balance": 3200},
}

def login():
    acc = input("Account No: ")
    pin = input("PIN: ")
    if acc in accounts and accounts[acc]["pin"] == pin:
        return accounts[acc]
    print("Invalid details!")
    return None

def atm():
    user = None
    while not user:
        user = login()

    print(f"\nWelcome {user['name']}!")

    while True:
        choice = input("\n1.Balance  2.Deposit  3.Withdraw  4.Exit : ")

        if choice == "1":
            print("Balance:", user["balance"])

        elif choice == "2":
            amt = float(input("Deposit amount: "))
            user["balance"] += amt
            print("Updated Balance:", user["balance"])

        elif choice == "3":
            amt = float(input("Withdraw amount: "))
            if amt <= user["balance"]:
                user["balance"] -= amt
                print("Updated Balance:", user["balance"])
            else:
                print("Insufficient balance!")

        elif choice == "4":
            print("Thank you!")
            break

atm()