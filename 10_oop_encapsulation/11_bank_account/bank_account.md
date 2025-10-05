# 🏦 Python OOP Practice - Lesson 26: BankAccount Class

## 📝 Exercise: Classic Encapsulation with Banking Operations

Create a `BankAccount` class that demonstrates the fundamental principles of encapsulation through secure banking operations. This is the classic example used to teach encapsulation concepts.

**Instructions:**
Implement a bank account that protects the balance from invalid operations while providing safe methods for deposits and withdrawals.

The account should maintain data integrity by preventing negative balances and invalid transaction amounts.

This exercise demonstrates why encapsulation is essential for protecting critical business data.

**Your Complete Task:**
1. Create a `BankAccount` class with constructor parameters:
   - `account_holder` (string): Name of the account holder
   - `initial_balance` (float): Starting balance (default 0.0, must be non-negative)
2. Store balance privately with underscore prefix (`_balance`)
3. Add `get_account_holder()` method (read-only after creation)
4. Add `get_balance()` method (read-only) that returns current balance
5. Add `deposit(amount)` method that adds money to the account
6. Add `withdraw(amount)` method that removes money if sufficient funds available
7. Add `transfer(amount, target_account)` method that transfers money to another account
8. Add proper validation with `ValueError` for invalid operations:
   - Negative or zero amounts for deposits/withdrawals
   - Insufficient funds for withdrawals
   - Invalid initial balance
9. Add `__str__()` method that returns account information

**What You'll Learn:**
- **Data Protection:** Preventing direct modification of critical data
- **Business Rules:** Enforcing banking constraints and validation
- **Transaction Safety:** Ensuring operations maintain data integrity
- **Read-Only Methods:** Exposing data without allowing modification
- **Method Validation:** Comprehensive input checking and error handling

**Business Rules:**
- Balance cannot go negative
- Deposit and withdrawal amounts must be positive
- Initial balance must be non-negative
- Transfer operations are atomic (either both succeed or both fail)

**Example Usage:**
```python
# Create accounts
alice_account = BankAccount("Alice", 1000.0)
bob_account = BankAccount("Bob", 500.0)

print(alice_account)  # "Account holder: Alice, Balance: $1000.00"
print(alice_account.get_balance())  # 1000.0

# Deposit money
alice_account.deposit(250.0)
print(alice_account.get_balance())  # 1250.0

# Withdraw money
alice_account.withdraw(100.0)
print(alice_account.get_balance())  # 1150.0

# Transfer money
alice_account.transfer(200.0, bob_account)
print(alice_account.get_balance())  # 950.0
print(bob_account.get_balance())    # 700.0

# Invalid operations (should raise ValueError)
try:
    alice_account.withdraw(2000.0)  # Insufficient funds
except ValueError as e:
    print(e)  # "Insufficient funds. Balance: $950.00, Attempted withdrawal: $2000.00"

try:
    alice_account.deposit(-50.0)  # Negative deposit
except ValueError as e:
    print(e)  # "Deposit amount must be positive"

try:
    bob_account.withdraw(0)  # Zero withdrawal
except ValueError as e:
    print(e)  # "Withdrawal amount must be positive"

# Invalid account creation
try:
    invalid_account = BankAccount("Charlie", -100.0)
except ValueError as e:
    print(e)  # "Initial balance cannot be negative"
```

**Key Encapsulation Concepts:**
- **Private Data:** `_balance` is protected from direct access
- **Controlled Access:** Balance can only be modified through safe methods
- **Data Integrity:** Business rules prevent invalid states
- **Read-Only Interface:** Balance and account holder are read-only getter methods