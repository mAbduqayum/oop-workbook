class BankAccount:
    """
    A BankAccount class with no encapsulation.
    The balance can be changed by anyone, to anything.
    """

    def __init__(self, account_holder, balance) -> None:
        self.account_holder = account_holder
        self.balance = balance


# --- Usage Example ---

# Create multiple accounts
alice_account = BankAccount("Alice Johnson", 1000.0)
bob_account = BankAccount("Bob Smith", 500.0)
charlie_account = BankAccount("Charlie Brown", 750.0)

print("=== Initial Account States ===")
print(f"Alice: ${alice_account.balance:.2f}")
print(f"Bob: ${bob_account.balance:.2f}")
print(f"Charlie: ${charlie_account.balance:.2f}")
print()

# === Transaction 1: Alice transfers $200 to Bob ===
print("=== Transaction 1: Alice transfers $200 to Bob ===")
print("Without encapsulation, we have to manually handle both sides:")
print("1. Subtracting from Alice...")
alice_account.balance -= 200.0
print(f"   Alice's balance: ${alice_account.balance:.2f}")

print("2. Adding to Bob...")
bob_account.balance += 200.0
print(f"   Bob's balance: ${bob_account.balance:.2f}")
print()

# === Transaction 2: Bob transfers $150 to Charlie (with a mistake!) ===
print("=== Transaction 2: Bob transfers $150 to Charlie ===")
print("OOPS! Developer forgot to subtract from Bob's account!")
print("1. Adding to Charlie...")
charlie_account.balance += 150.0
print(f"   Charlie's balance: ${charlie_account.balance:.2f}")
print("2. Forgetting to subtract from Bob... (MONEY CREATED FROM THIN AIR!)")
print(f"   Bob's balance: ${bob_account.balance:.2f} (should be $550!)")
print()

# === Transaction 3: Charlie transfers $300 to Alice (duplicate code) ===
print("=== Transaction 3: Charlie transfers $300 to Alice ===")
print("More duplicate code with potential for errors:")
print("1. Subtracting from Charlie...")
charlie_account.balance -= 300.0
print(f"   Charlie's balance: ${charlie_account.balance:.2f}")

print("2. Adding to Alice...")
alice_account.balance += 300.0
print(f"   Alice's balance: ${alice_account.balance:.2f}")
print()

# === The Big Problem: Direct manipulation ===
print("=== The Big Problem: Anyone can manipulate balances directly ===")
print("Setting Alice's balance to -999.0...")
alice_account.balance = -999.0
print(f"Alice's balance: ${alice_account.balance:.2f}")
print("The bank would NEVER allow this!")
print()

print("=== Final (Invalid) Account States ===")
print(f"Alice: ${alice_account.balance:.2f} (NEGATIVE!)")
print(f"Bob: ${bob_account.balance:.2f} (Got free money!)")
print(f"Charlie: ${charlie_account.balance:.2f}")
print()
print("🚨 PROBLEMS WITH UNENCAPSULATED CODE:")
print("  • Forgot to subtract from Bob's account (duplicate transaction logic)")
print("  • Direct access allowed invalid negative balance")
print("  • No validation or constraints")
print("  • Easy to make mistakes with manual two-step transfers")
