# 🏦 Python OOP Practice - Lesson: Bank Account Class

## 📝 Exercise: Create a Banking System

Create a `BankAccount` class that manages money with safety checks and calculated properties. This introduces data validation and computed values.

**Your Complete Task:**
1. Create a `BankAccount` class with `owner_name` and `balance` attributes (balance starts at 0)
2. Add a `deposit(amount)` method that adds money and prints "Deposited $[amount]. New balance: $[balance]"
3. Add a `withdraw(amount)` method that checks if sufficient funds exist:
   - If yes: subtract amount and print "Withdrew $[amount]. New balance: $[balance]"
   - If no: print "Insufficient funds! Current balance: $[balance]"
4. Add a `get_balance()` method that returns the current balance
5. Add an `account_info()` method that prints "Account holder: [name], Balance: $[balance]"
6. Create 2 bank accounts, perform various deposits and withdrawals, and display account information

**What You'll Learn:**
- Data validation in methods (checking sufficient funds)
- Methods that return values vs. methods that print
- Protecting object state with business logic
- Real-world class design patterns
- Error handling in object methods

**Example Usage:**
```python
# Create 2 bank accounts
account1 = BankAccount("Alice")
account2 = BankAccount("Bob")

# Test Alice's account
account1.account_info()  # Account holder: Alice, Balance: $0
account1.deposit(100)    # Deposited $100. New balance: $100
account1.withdraw(30)    # Withdrew $30. New balance: $70
account1.account_info()  # Account holder: Alice, Balance: $70

# Test Bob's account
account2.account_info()  # Account holder: Bob, Balance: $0
account2.deposit(50)     # Deposited $50. New balance: $50
account2.withdraw(75)    # Insufficient funds! Current balance: $50
account2.account_info()  # Account holder: Bob, Balance: $50
```

