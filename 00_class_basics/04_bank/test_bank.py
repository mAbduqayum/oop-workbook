import unittest

from bank import BankAccount


class TestBankAccount(unittest.TestCase):
    def test_account_creation(self):
        account = BankAccount("Alice")
        self.assertEqual(account.owner_name, "Alice")
        self.assertEqual(account.balance, 0)

    def test_deposit(self):
        account = BankAccount("Bob")
        account.deposit(100)
        self.assertEqual(account.balance, 100)

    def test_withdraw_sufficient_funds(self):
        account = BankAccount("Charlie")
        account.deposit(100)
        account.withdraw(30)
        self.assertEqual(account.balance, 70)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("Dave")
        account.deposit(50)
        account.withdraw(80)
        self.assertEqual(account.balance, 50)


if __name__ == "__main__":
    unittest.main()
