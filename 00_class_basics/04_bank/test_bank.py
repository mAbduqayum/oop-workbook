from bank import BankAccount


class TestBankAccount:
    def test_account_creation(self):
        account = BankAccount("Alice")
        assert account.owner_name == "Alice"
        assert account.balance == 0

    def test_deposit(self):
        account = BankAccount("Bob")
        account.deposit(100)
        assert account.balance == 100

    def test_withdraw_sufficient_funds(self):
        account = BankAccount("Charlie")
        account.deposit(100)
        account.withdraw(30)
        assert account.balance == 70

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("Dave")
        account.deposit(50)
        account.withdraw(80)
        assert account.balance == 50
