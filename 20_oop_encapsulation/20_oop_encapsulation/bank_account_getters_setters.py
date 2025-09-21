class BankAccountA:
    """
    This solution uses explicit 'getter' and 'setter' methods
    to protect the _balance attribute and provides safe transfer methods.
    """

    def __init__(self, account_holder, balance) -> None:
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
            print(f"✅ Balance successfully set to ${amount:.2f}")
        else:
            print("❌ Error: Invalid amount. Balance was not changed.")

    def deposit(self, amount):
        """Safely add money to the account."""
        if isinstance(amount, (int, float)) and amount > 0:
            self._balance += amount
            print(f"✅ Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")
            return True
        else:
            print("❌ Error: Invalid deposit amount.")
            return False

    def withdraw(self, amount):
        """Safely remove money from the account."""
        if isinstance(amount, (int, float)) and amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"✅ Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")
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
        """
        if not isinstance(recipient_account, BankAccountA):
            print("❌ Error: Invalid recipient account.")
            return False

        if isinstance(amount, (int, float)) and amount > 0:
            if self._balance >= amount:
                # Both operations must succeed
                self._balance -= amount
                recipient_account._balance += amount
                print(
                    f"✅ Transferred ${amount:.2f} from {self.account_holder} to {recipient_account.account_holder}"
                )
                print(f"   {self.account_holder}: ${self._balance:.2f}")
                print(
                    f"   {recipient_account.account_holder}: ${recipient_account._balance:.2f}"
                )
                return True
            else:
                print(
                    f"❌ Error: Insufficient funds for transfer. Balance: ${self._balance:.2f}"
                )
                return False
        else:
            print("❌ Error: Invalid transfer amount.")
            return False


# --- Usage Example ---

# Create multiple accounts with encapsulation
alice_account = BankAccountA("Alice Johnson", 1000.0)
bob_account = BankAccountA("Bob Smith", 500.0)
charlie_account = BankAccountA("Charlie Brown", 750.0)

print("=== Initial Account States (Using Getters) ===")
print(f"Alice: ${alice_account.get_balance():.2f}")
print(f"Bob: ${bob_account.get_balance():.2f}")
print(f"Charlie: ${charlie_account.get_balance():.2f}")
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

print("Attempting to set Alice's balance to -500...")
alice_account.set_balance(-500.0)
print()

print("=== Final Account States ===")
print(f"Alice: ${alice_account.get_balance():.2f}")
print(f"Bob: ${bob_account.get_balance():.2f}")
print(f"Charlie: ${charlie_account.get_balance():.2f}")
print()
print("✅ BENEFITS OF ENCAPSULATION WITH GETTERS/SETTERS:")
print("  • Transfer is atomic - can't forget the second step")
print("  • Validation prevents invalid states")
print("  • Consistent interface for all operations")
print("  • No duplicate transaction logic")
