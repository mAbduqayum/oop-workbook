class BankAccountB:
    """
    This solution uses the Pythonic @property decorator to
    achieve encapsulation with a cleaner syntax and provides safe transfer methods.
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
            print(f"✅ Balance successfully set to ${amount:.2f}")
        else:
            print("❌ Error: Invalid amount. Balance was not changed.")

    def deposit(self, amount):
        """Safely add money to the account using property setter."""
        if isinstance(amount, (int, float)) and amount > 0:
            old_balance = self._balance
            self._balance += amount
            print(f"✅ Deposited ${amount:.2f}. Balance: ${old_balance:.2f} → ${self._balance:.2f}")
            return True
        else:
            print("❌ Error: Invalid deposit amount.")
            return False

    def withdraw(self, amount):
        """Safely remove money from the account."""
        if isinstance(amount, (int, float)) and amount > 0:
            if self._balance >= amount:
                old_balance = self._balance
                self._balance -= amount
                print(f"✅ Withdrew ${amount:.2f}. Balance: ${old_balance:.2f} → ${self._balance:.2f}")
                return True
            else:
                print(f"❌ Error: Insufficient funds. Balance: ${self._balance:.2f}")
                return False
        else:
            print("❌ Error: Invalid withdrawal amount.")
            return False

    def transfer_to(self, recipient_account, amount):
        """
        Transfer money to another account safely.
        This encapsulates the two-step process into one atomic operation.
        Uses property access for clean, readable code.
        """
        if not isinstance(recipient_account, BankAccountB):
            print("❌ Error: Invalid recipient account.")
            return False

        if isinstance(amount, (int, float)) and amount > 0:
            if self.balance >= amount:  # Using property getter
                # Both operations must succeed
                self._balance -= amount
                recipient_account._balance += amount
                print(f"✅ Transferred ${amount:.2f} from {self.account_holder} to {recipient_account.account_holder}")
                print(f"   {self.account_holder}: ${self.balance:.2f}")  # Using property getter
                print(f"   {recipient_account.account_holder}: ${recipient_account.balance:.2f}")  # Using property getter
                return True
            else:
                print(f"❌ Error: Insufficient funds for transfer. Balance: ${self.balance:.2f}")
                return False
        else:
            print("❌ Error: Invalid transfer amount.")
            return False

# --- Usage Example ---

# Create multiple accounts with Pythonic encapsulation
alice_account = BankAccountB("Alice Johnson", 1000.0)
bob_account = BankAccountB("Bob Smith", 500.0)
charlie_account = BankAccountB("Charlie Brown", 750.0)

print("=== Initial Account States (Using Properties) ===")
print(f"Alice: ${alice_account.balance:.2f}")    # Clean property access
print(f"Bob: ${bob_account.balance:.2f}")        # Clean property access
print(f"Charlie: ${charlie_account.balance:.2f}") # Clean property access
print()

# === Transaction 1: Alice transfers $200 to Bob ===
print("=== Transaction 1: Alice transfers $200 to Bob ===")
alice_account.transfer_to(bob_account, 200.0)
print()

# === Transaction 2: Bob transfers $150 to Charlie ===
print("=== Transaction 2: Bob transfers $150 to Charlie ===")
bob_account.transfer_to(charlie_account, 150.0)
print()

# === Transaction 3: Charlie transfers $300 to Alice ===
print("=== Transaction 3: Charlie transfers $300 to Alice ===")
charlie_account.transfer_to(alice_account, 300.0)
print()

# === Test validation ===
print("=== Testing Validation ===")
print("Attempting to transfer $999999 from Charlie to Bob...")
charlie_account.transfer_to(bob_account, 999999.0)
print()

print("Attempting to set Alice's balance to -500 using property...")
alice_account.balance = -500.0  # This will trigger the @balance.setter
print()

print("=== Final Account States ===")
print(f"Alice: ${alice_account.balance:.2f}")
print(f"Bob: ${bob_account.balance:.2f}")
print(f"Charlie: ${charlie_account.balance:.2f}")
print()
print("✅ BENEFITS OF ENCAPSULATION WITH PROPERTIES:")
print("  • Clean, intuitive syntax (account.balance vs account.get_balance())")
print("  • Transfer is atomic - can't forget the second step")
print("  • Validation happens automatically via setters")
print("  • Pythonic and readable code")
print("  • No duplicate transaction logic")
