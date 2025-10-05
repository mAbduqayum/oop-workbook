class BankAccount:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Balance: ${self.balance}")
        else:
            print(f"Insufficient funds! Balance: ${self.balance}")


if __name__ == "__main__":
    account = BankAccount("Alice")
    account.deposit(100)
    account.withdraw(30)
    account.withdraw(80)
