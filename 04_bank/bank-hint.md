# 💡 Hints for Bank Account Exercise

## Setting Up the Class
- Constructor takes only `owner_name` as parameter
- Set `self.balance = 0` to start with empty account
- Store owner name: `self.owner_name = owner_name`

## Deposit Method
- Add the amount to current balance: `self.balance += amount`
- Print confirmation with new total
- No validation needed - assume positive amounts

## Withdraw Method Logic
- Check BEFORE withdrawing: `if self.balance >= amount:`
- If enough money: subtract and print success message
- If not enough: print error message with current balance
- Use `else:` for the insufficient funds case

## Methods That Return vs Print
- `get_balance()` should `return self.balance` (no print)
- `account_info()` should print formatted string
- Returning means other code can use the value

## Testing Your Methods
- Create account with 0 balance
- Try deposit, check balance goes up
- Try valid withdrawal, check balance goes down
- Try invalid withdrawal, check balance stays same
- Test account_info() shows correct information

## String Formatting Tips
- Use f-strings for cleaner code: `f"Balance: ${self.balance}"`
- Remember the $ symbol for money formatting

## Method Organization
1. `__init__` - sets up the account
2. `deposit` - adds money
3. `withdraw` - removes money (with check)
4. `get_balance` - returns current amount
5. `account_info` - displays summary

## Common Mistakes
- Don't forget to update `self.balance` in deposit/withdraw
- Check funds BEFORE subtracting in withdraw
- Return vs print - get_balance returns, others print
