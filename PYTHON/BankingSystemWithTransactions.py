import random
class OverdraftError(Exception):
    pass
class TransactionTimeoutError(Exception):
    pass
class InvalidAccountNumberError(Exception):
    pass
class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise OverdraftError("Insufficient balance.")
        self.balance -= amount


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, holder_name, balance=0):
        if len(account_number) != 6 or not account_number.isdigit():
            raise InvalidAccountNumberError("Account number must be a 6-digit number.")

        self.accounts[account_number] = BankAccount(account_number, holder_name, balance)
        print("Account created successfully.")

    def transfer(self, sender_acc, receiver_acc, amount):
        if sender_acc not in self.accounts or receiver_acc not in self.accounts:
            raise InvalidAccountNumberError("One or both account numbers are invalid.")
        if random.choice([False, False, True]):
            raise TransactionTimeoutError("Transaction failed due to timeout.")

        sender = self.accounts[sender_acc]
        receiver = self.accounts[receiver_acc]

        sender.withdraw(amount)
        receiver.deposit(amount)

        print("Transaction completed successfully.")

    def show_account(self, account_number):
        if account_number not in self.accounts:
            raise InvalidAccountNumberError("Account number not found.")

        acc = self.accounts[account_number]
        print(f"Account No: {acc.account_number}")
        print(f"Holder Name: {acc.holder_name}")
        print(f"Balance: {acc.balance}")


def main():
    bank = BankSystem()

    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Transfer Money")
        print("3. View Account")
        print("4. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                acc_no = input("Enter 6-digit account number: ")
                name = input("Enter holder name: ")
                balance = float(input("Enter initial balance: "))
                bank.create_account(acc_no, name, balance)

            elif choice == "2":
                sender = input("Enter sender account number: ")
                receiver = input("Enter receiver account number: ")
                amount = float(input("Enter amount to transfer: "))
                bank.transfer(sender, receiver, amount)

            elif choice == "3":
                acc_no = input("Enter account number: ")
                bank.show_account(acc_no)

            elif choice == "4":
                print("Exiting Banking System.")
                break

            else:
                print("Invalid choice.")

        except (OverdraftError, TransactionTimeoutError, InvalidAccountNumberError, ValueError) as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()