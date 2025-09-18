# 02_solution_getters_setters.py

class BankAccountA:
    """
    This solution uses explicit 'getter' and 'setter' methods
    to protect the _balance attribute.
    """
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        # "Private" attribute for internal use
        self._balance = balance

    # Getter: A public method to READ the data
    def get_balance(self):
        return self._balance

    # Setter: A public method to WRITE the data, with rules
    def set_balance(self, amount):
        if isinstance(amount, (int, float)) and amount >= 0:
            self._balance = amount
            print(f"Balance successfully set to ${amount:.2f}")
        else:
            print("Error: Invalid amount. Balance was not changed.")

# --- Usage Example ---

my_account = BankAccountA("Jane Doe", 100.0)

# We must use the methods now
print(f"Account Holder: {my_account.account_holder}")
print(f"Initial Balance: ${my_account.get_balance():.2f}")

print("-" * 20)

# Let's try to set a negative balance
print("Attempting to set balance to -500.0...")
my_account.set_balance(-500.0)

# The balance remains unchanged and protected
print(f"Final balance: ${my_account.get_balance():.2f}")
