# 💡 Hints for Car Class Exercise

## Multiple Attributes Setup
- Constructor needs `brand`, `model` parameters
- Initialize fuel to 0: `self.fuel = 0`
- No need to pass fuel as parameter

## Methods That Change State
- `add_fuel()` should modify `self.fuel`
- Use `+=` to increase: `self.fuel += amount`
- Always update the attribute, then print the result

## Methods With Parameters
- `add_fuel(self, amount)` - don't forget `self` first!
- Use the parameter inside the method: `self.fuel += amount`

## Conditional Logic in Methods
- `drive()` should check `if self.fuel > 0:`
- If true: decrease fuel and print driving message
- If false: print "no fuel" message

## String Formatting with Multiple Attributes
- Use f-strings: `f"Driving the {self.brand} {self.model}!"`
- Access multiple attributes in one string

## State Changes
- Each method call can change the object's state
- Fuel goes up with `add_fuel()`, down with `drive()`
- Each car tracks its own fuel independently

## Testing Your Code
1. Create cars
2. Start engines (doesn't need fuel)
3. Add fuel before driving
4. Try driving multiple times to see fuel decrease
5. Try driving with no fuel to test your condition

## Common Gotchas
- Don't forget `self` parameter in all methods
- Remember to actually modify `self.fuel` in methods
- Check fuel BEFORE trying to drive