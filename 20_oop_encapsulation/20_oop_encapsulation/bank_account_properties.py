# 03_solution_properties.py

class BankAccountB:
    """
    This solution uses the Pythonic @property decorator to
    achieve encapsulation with a cleaner syntax.
    """
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        # "Private" attribute for internal use
        self._balance = balance

    @property
    def balance(self):
        """This is the 'getter'. It runs when you READ my_account.balance."""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """This is the 'setter'. It runs when you WRITE to my_account.balance."""
        if isinstance(amount, (int, float)) and amount >= 0:
            self._balance = amount
            print(f"Balance successfully set to ${amount:.2f}")
        else:
            print("Error: Invalid amount. Balance was not changed.")

# --- Usage Example ---

my_account = BankAccountB("Will Smith", 200.0)

# 1. Reading the balance (looks like a variable, but runs the getter)
print(f"Account Holder: {my_account.account_holder}")
print(f"Initial Balance: ${my_account.balance:.2f}")

print("-" * 20)

# 2. Trying to set a negative balance (looks like a variable, but runs the setter)
print("Attempting to set balance to -500.0...")
my_account.balance = -500.0

# 3. The balance remains unchanged and protected
print(f"Final balance: ${my_account.balance:.2f}")
