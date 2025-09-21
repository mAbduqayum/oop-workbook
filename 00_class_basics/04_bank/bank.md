## Exercise: Bank Account Class

Create a `BankAccount` class that manages money with safety checks.

### Your Task:
1. Create a `BankAccount` class with `owner_name` and `balance` attributes (balance starts at 0)
2. Add a `deposit(amount)` method that adds money and prints `f"Balance: ${balance}"`
3. Add a `withdraw(amount)` method that checks if sufficient funds exist:
   - If yes: subtract amount and print `f"Balance: ${balance}"`
   - If no: print `f"Insufficient funds! Balance: ${balance}"`

### Example Usage:
```python
account = BankAccount("Alice")
account.deposit(100)    # Balance: $100
account.withdraw(30)    # Balance: $70
account.withdraw(80)    # Insufficient funds! Balance: $70
```

