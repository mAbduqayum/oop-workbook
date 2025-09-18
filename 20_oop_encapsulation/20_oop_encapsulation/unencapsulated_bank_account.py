# 01_problem_unencapsulated.py

class BankAccount:
    """
    A BankAccount class with no encapsulation.
    The balance can be changed by anyone, to anything.
    """
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

# --- Usage Example ---

# Create an account
my_account = BankAccount("John Doe", 100.0)
print(f"Account Holder: {my_account.account_holder}")
print(f"Initial Balance: ${my_account.balance:.2f}")

print("-" * 20)

# The problem: Direct access allows for invalid changes
print("Setting balance to -500.0...")
my_account.balance = -500.0 # The bank would never allow this!

print(f"New balance: ${my_account.balance:.2f}")
print("The object is now in an invalid state.")
