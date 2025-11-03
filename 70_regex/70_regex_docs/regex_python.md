# Python Regex Module Reference (`re`)

Complete reference for Python's built-in `re` module for regular expression operations.

> **See also**: [`regex.md`](./regex.md) for general regex syntax and patterns

---

## Table of Contents

1. [Introduction](#introduction)
2. [Module-Level Functions](#module-level-functions)
3. [Compilation Flags](#compilation-flags)
4. [Pattern Objects](#pattern-objects)
5. [Match Objects](#match-objects)
6. [Key Differences](#key-differences)
7. [Quick Reference](#quick-reference)

---

## Introduction

### When to Use Regex vs String Methods

| Use Regex When...                          | Use String Methods When...         |
|--------------------------------------------|------------------------------------|
| Pattern matching with wildcards/variations | Exact literal matching             |
| Complex validation (email, phone, etc.)    | Simple contains/starts/ends checks |
| Extracting structured data                 | Splitting by single delimiter      |
| Advanced find/replace with patterns        | Simple literal replacement         |

### Raw Strings in Python

**Always use raw strings (`r""`) for regex patterns** to avoid double-escaping:

```python
# WRONG: Single backslash gets escaped by Python
pattern = '\d+'  # Actually becomes '\\d+' - matches literal \d+

# RIGHT: Raw string preserves backslashes
pattern = r'\d+'  # Stays as '\d+' - matches digits

# Alternative: Double-escape (not recommended)
pattern = '\\d+'  # Works but harder to read
```

---

## Module-Level Functions

### Pattern Matching Functions

| Function                                 | Description                             | Returns              | When to Use            |
|------------------------------------------|-----------------------------------------|----------------------|------------------------|
| `re.search(pattern, string, flags=0)`    | Scan for first match anywhere in string | Match object or None | Find pattern anywhere  |
| `re.match(pattern, string, flags=0)`     | Check only at string start              | Match object or None | Validate string prefix |
| `re.fullmatch(pattern, string, flags=0)` | Match entire string                     | Match object or None | Validate entire string |

**Examples:**

```python
import re

text = "The price is $25.99"

# search() - finds pattern anywhere
re.search(r'\d+\.\d{2}', text)  # Matches '25.99'

# match() - only checks string start
re.match(r'\d+\.\d{2}', text)  # None (doesn't start with number)
re.match(r'The', text)  # Matches 'The'

# fullmatch() - entire string must match
re.fullmatch(r'\d+\.\d{2}', '25.99')  # Matches
re.fullmatch(r'\d+\.\d{2}', text)  # None (extra text)
```

### Finding All Matches

| Function                                | Description                | Returns                   | Memory Usage        |
|-----------------------------------------|----------------------------|---------------------------|---------------------|
| `re.findall(pattern, string, flags=0)`  | Return all matches as list | List of strings or tuples | Loads all in memory |
| `re.finditer(pattern, string, flags=0)` | Iterator of Match objects  | Iterator of Match objects | Memory efficient    |

**Examples:**

```python
text = "Contact: alice@example.com or bob@test.org"
pattern = r'\w+@\w+\.\w+'

# findall() - returns list of strings
emails = re.findall(pattern, text)
# ['alice@example.com', 'bob@test.org']

# finditer() - returns iterator of Match objects
for match in re.finditer(pattern, text):
    print(f"Found {match.group()} at position {match.start()}")
# Found alice@example.com at position 9
# Found bob@test.org at position 30
```

**With capturing groups:**

```python
pattern = r'(\w+)@(\w+\.\w+)'

# findall() returns tuples when pattern has groups
re.findall(pattern, text)
# [('alice', 'example.com'), ('bob', 'test.org')]

# finditer() returns Match objects with group access
for match in re.finditer(pattern, text):
    print(f"User: {match.group(1)}, Domain: {match.group(2)}")
```

### String Modification Functions

| Function                                           | Description                                    | Returns                         |
|----------------------------------------------------|------------------------------------------------|---------------------------------|
| `re.sub(pattern, repl, string, count=0, flags=0)`  | Replace matches with string or function result | Modified string                 |
| `re.subn(pattern, repl, string, count=0, flags=0)` | Same as `sub()` but also returns count         | Tuple: (modified_string, count) |
| `re.split(pattern, string, maxsplit=0, flags=0)`   | Split string by pattern                        | List of strings                 |

**Examples:**

```python
text = "Price: $25.99, Tax: $3.12"

# sub() - replace matches
result = re.sub(r'\$(\d+\.\d{2})', r'USD \1', text)


# 'Price: USD 25.99, Tax: USD 3.12'

# sub() with function replacement
def format_price(match):
    amount = float(match.group(1))
    return f"€{amount * 0.85:.2f}"


result = re.sub(r'\$(\d+\.\d{2})', format_price, text)
# 'Price: €22.09, Tax: €2.65'

# subn() - replace and count
result, count = re.subn(r'\$\d+\.\d{2}', 'PRICE', text)
# ('Price: PRICE, Tax: PRICE', 2)

# split() - split by pattern
text = "apple,banana;  cherry|grape"
fruits = re.split(r'[,;|]\s*', text)
# ['apple', 'banana', 'cherry', 'grape']

# split() with capturing groups (groups are included in result)
parts = re.split(r'(\s+)', "hello   world")
# ['hello', '   ', 'world']
```

### Utility Functions

| Function                       | Description                       | Use Case                         |
|--------------------------------|-----------------------------------|----------------------------------|
| `re.compile(pattern, flags=0)` | Compile pattern to Pattern object | Reuse pattern multiple times     |
| `re.escape(pattern)`           | Escape all metacharacters         | Match literal special characters |
| `re.purge()`                   | Clear internal regex cache        | Free memory (rarely needed)      |

**Examples:**

```python
# compile() - for pattern reuse (more efficient)
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
for line in lines:
    if pattern.search(line):
        print(line)

# escape() - make special characters literal
user_input = "How much is 2+2?"
safe_pattern = re.escape(user_input)
# 'How\\ much\\ is\\ 2\\+2\\?'
re.search(safe_pattern, text)  # Matches literal "How much is 2+2?"
```

---

## Compilation Flags

Flags modify regex behavior. Combine with `|` operator: `re.I | re.M`

| Flag        | Alias           | Description                                          | Example                         |
|-------------|-----------------|------------------------------------------------------|---------------------------------|
| `re.A`      | `re.ASCII`      | Make `\w`, `\d`, `\s` match ASCII only (not Unicode) | Match only ASCII letters        |
| `re.I`      | `re.IGNORECASE` | Case-insensitive matching                            | Match 'Hello', 'HELLO', 'hello' |
| `re.L`      | `re.LOCALE`     | Make `\w`, `\d`, `\s` locale-dependent (bytes only)  | Legacy byte patterns            |
| `re.M`      | `re.MULTILINE`  | `^` and `$` match at line boundaries                 | Multi-line text processing      |
| `re.S`      | `re.DOTALL`     | `.` matches newline characters                       | Patterns spanning lines         |
| `re.X`      | `re.VERBOSE`    | Allow whitespace and comments in pattern             | Complex, readable patterns      |
| `re.DEBUG`  | -               | Display compilation debug information                | Pattern debugging               |
| `re.NOFLAG` | -               | No flags (explicit default)                          | Code clarity                    |

### Flag Examples

```python
# Case-insensitive matching
re.search(r'hello', 'HELLO', re.I)  # Matches

# Multiline mode: ^ and $ match line boundaries
text = "line1\nline2\nline3"
re.findall(r'^line', text)  # ['line1'] - only string start
re.findall(r'^line', text, re.M)  # ['line1', 'line2', 'line3']

# DOTALL: . matches newlines
text = "line1\nline2"
re.search(r'line1.line2', text)  # None (. doesn't match \n)
re.search(r'line1.line2', text, re.S)  # Matches

# VERBOSE: readable complex patterns
pattern = re.compile(r'''
    ^                   # Start of string
    (?P<area>\d{3})     # Area code
    -                   # Separator
    (?P<prefix>\d{3})   # Prefix
    -                   # Separator
    (?P<line>\d{4})     # Line number
    $                   # End of string
''', re.VERBOSE)

# Combining flags
re.search(r'^hello', 'HELLO', re.I | re.M)

# Inline flags (in pattern itself)
re.search(r'(?i)hello', 'HELLO')  # Equivalent to re.I
```

---

## Pattern Objects

Created by `re.compile()` for efficient pattern reuse.

### Creating Pattern Objects

```python
# Compile once, reuse many times
pattern = re.compile(r'\d{3}-\d{3}-\d{4}', re.VERBOSE)

# Use like module functions
pattern.search(text)
pattern.findall(text)
pattern.sub(replacement, text)
```

### Pattern Methods

Same as module functions but with optional `pos` and `endpos` parameters:

| Method                                       | Description           | Extra Parameters    |
|----------------------------------------------|-----------------------|---------------------|
| `Pattern.search(string[, pos[, endpos]])`    | Search in string      | Start/end positions |
| `Pattern.match(string[, pos[, endpos]])`     | Match at string start | Start/end positions |
| `Pattern.fullmatch(string[, pos[, endpos]])` | Match entire string   | Start/end positions |
| `Pattern.findall(string[, pos[, endpos]])`   | Find all matches      | Start/end positions |
| `Pattern.finditer(string[, pos[, endpos]])`  | Iterator of matches   | Start/end positions |
| `Pattern.split(string, maxsplit=0)`          | Split by pattern      | Max splits          |
| `Pattern.sub(repl, string, count=0)`         | Replace matches       | Max replacements    |
| `Pattern.subn(repl, string, count=0)`        | Replace and count     | Max replacements    |

**Using pos and endpos:**

```python
pattern = re.compile(r'\d+')
text = "abc 123 def 456 ghi"

# Search in substring [4:11] only
match = pattern.search(text, 4, 11)  # Matches '123'
match.group()  # '123'
```

### Pattern Attributes

| Attribute            | Description                         | Example                    |
|----------------------|-------------------------------------|----------------------------|
| `Pattern.pattern`    | Original pattern string             | `r'\d+'`                   |
| `Pattern.flags`      | Compilation flags used              | `re.IGNORECASE`            |
| `Pattern.groups`     | Number of capturing groups          | `3`                        |
| `Pattern.groupindex` | Dict mapping group names to numbers | `{'area': 1, 'prefix': 2}` |

**Example:**

```python
pattern = re.compile(r'(?P<user>\w+)@(?P<domain>\w+\.\w+)', re.I)

print(pattern.pattern)  # '(?P<user>\\w+)@(?P<domain>\\w+\\.\\w+)'
print(pattern.flags)  # re.IGNORECASE
print(pattern.groups)  # 2
print(pattern.groupindex)  # {'user': 1, 'domain': 2}
```

---

## Match Objects

Returned by successful `search()`, `match()`, `fullmatch()`, and `finditer()`.

### Extracting Data

| Method                          | Description                    | Example                           |
|---------------------------------|--------------------------------|-----------------------------------|
| `Match.group([group1, ...])`    | Get matched substring(s)       | `m.group(1)` or `m.group('name')` |
| `Match.groups(default=None)`    | Tuple of all captured groups   | `(group1, group2, ...)`           |
| `Match.groupdict(default=None)` | Dict of named groups           | `{'name': value, ...}`            |
| `Match[g]`                      | Bracket notation (Python 3.6+) | `m[1]` same as `m.group(1)`       |

**Examples:**

```python
pattern = r'(?P<user>\w+)@(?P<domain>\w+\.\w+)'
match = re.search(pattern, "Email: alice@example.com")

# group() - access by number or name
match.group(0)  # 'alice@example.com' (entire match)
match.group(1)  # 'alice'
match.group(2)  # 'example.com'
match.group('user')  # 'alice'
match.group('domain')  # 'example.com'

# Multiple groups at once
match.group(1, 2)  # ('alice', 'example.com')

# groups() - all capturing groups as tuple
match.groups()  # ('alice', 'example.com')

# groupdict() - named groups as dict
match.groupdict()  # {'user': 'alice', 'domain': 'example.com'}

# Bracket notation (Python 3.6+)
match[0]  # 'alice@example.com'
match[1]  # 'alice'
match['user']  # 'alice'
```

### Position Information

| Method                 | Description                | Returns               |
|------------------------|----------------------------|-----------------------|
| `Match.start([group])` | Start index of match/group | Integer index         |
| `Match.end([group])`   | End index of match/group   | Integer index         |
| `Match.span([group])`  | Both start and end         | Tuple: `(start, end)` |

**Examples:**

```python
text = "Email: alice@example.com"
match = re.search(r'\w+@\w+\.\w+', text)

match.start()  # 7 (start of 'alice@example.com')
match.end()  # 24 (end of 'alice@example.com')
match.span()  # (7, 24)

# Extract using slice
email = text[match.start():match.end()]  # 'alice@example.com'
# Or simpler:
email = match.group()  # 'alice@example.com'
```

### Other Methods

| Method                   | Description                                    |
|--------------------------|------------------------------------------------|
| `Match.expand(template)` | Perform backreference substitution on template |

**Example:**

```python
match = re.search(r'(\w+)@(\w+)\.(\w+)', 'alice@example.com')
template = r'User: \1, Domain: \2.\3'
match.expand(template)  # 'User: alice, Domain: example.com'
```

### Match Attributes

| Attribute         | Description                             | Example Value                |
|-------------------|-----------------------------------------|------------------------------|
| `Match.string`    | Original string being matched           | `'Email: alice@example.com'` |
| `Match.re`        | Pattern object that produced this match | `<Pattern object>`           |
| `Match.pos`       | Start position passed to search         | `0`                          |
| `Match.endpos`    | End boundary passed to search           | `24`                         |
| `Match.lastindex` | Index of last matched group (or None)   | `2`                          |
| `Match.lastgroup` | Name of last matched group (or None)    | `'domain'`                   |

**Example:**

```python
pattern = re.compile(r'(?P<user>\w+)@(?P<domain>\w+\.\w+)')
text = "alice@example.com"
match = pattern.search(text)

print(match.string)  # 'alice@example.com'
print(match.re.pattern)  # '(?P<user>\\w+)@(?P<domain>\\w+\\.\\w+)'
print(match.pos)  # 0
print(match.endpos)  # 17
print(match.lastindex)  # 2
print(match.lastgroup)  # 'domain'
```

---

## Key Differences

### match() vs search() vs fullmatch()

| Function                     | Behavior                   | Equivalent Pattern                    |
|------------------------------|----------------------------|---------------------------------------|
| `match(pattern, string)`     | Check only at string start | `search('^' + pattern, string)`       |
| `search(pattern, string)`    | Scan entire string         | Pattern as-is                         |
| `fullmatch(pattern, string)` | Entire string must match   | `search('^' + pattern + '$', string)` |

**Example:**

```python
text = "The price is $25.99"
pattern = r'\d+\.\d{2}'

re.match(pattern, text)  # None (doesn't start with number)
re.search(pattern, text)  # Matches '25.99'
re.fullmatch(pattern, text)  # None (entire string doesn't match)

re.fullmatch(pattern, '25.99')  # Matches
```

### findall() vs finditer()

| Feature       | findall()                            | finditer()                           |
|---------------|--------------------------------------|--------------------------------------|
| Returns       | List of strings/tuples               | Iterator of Match objects            |
| Memory        | Loads all matches in memory          | Lazy evaluation                      |
| Position info | No                                   | Yes (via Match.start(), Match.end()) |
| Group access  | Limited (tuples for groups)          | Full (Match.group(), Match.groups()) |
| Best for      | Small result sets, simple extraction | Large texts, need positions          |

**Example:**

```python
text = "alice@example.com bob@test.org charlie@demo.net"
pattern = r'(\w+)@(\w+\.\w+)'

# findall() - returns tuples
results = re.findall(pattern, text)
# [('alice', 'example.com'), ('bob', 'test.org'), ('charlie', 'demo.net')]

# finditer() - returns Match objects with more info
for match in re.finditer(pattern, text):
    print(f"Email: {match.group(0)}")
    print(f"  User: {match.group(1)}")
    print(f"  Domain: {match.group(2)}")
    print(f"  Position: {match.start()}-{match.end()}")
```

### sub() vs subn()

| Feature  | sub()            | subn()                             |
|----------|------------------|------------------------------------|
| Returns  | Modified string  | Tuple: (modified_string, count)    |
| Use when | Only need result | Need to know how many replacements |

**Example:**

```python
text = "Price: $25.99, Tax: $3.12, Total: $29.11"

# sub() - just the result
result = re.sub(r'\$\d+\.\d{2}', 'PRICE', text)
# 'Price: PRICE, Tax: PRICE, Total: PRICE'

# subn() - result + count
result, count = re.subn(r'\$\d+\.\d{2}', 'PRICE', text)
# ('Price: PRICE, Tax: PRICE, Total: PRICE', 3)
print(f"Made {count} replacements")
```

### Greedy vs Non-Greedy Quantifiers

| Quantifier              | Behavior                                 | Example                 |
|-------------------------|------------------------------------------|-------------------------|
| `*` `+` `?` `{m,n}`     | Greedy (match as much as possible)       | `.*` matches everything |
| `*?` `+?` `??` `{m,n}?` | Non-greedy (match as little as possible) | `.*?` matches minimally |

**Example:**

```python
html = '<div>Hello</div><div>World</div>'

# Greedy: matches across both divs
re.findall(r'<div>.*</div>', html)
# ['<div>Hello</div><div>World</div>']

# Non-greedy: matches each div separately
re.findall(r'<div>.*?</div>', html)
# ['<div>Hello</div>', '<div>World</div>']
```

---

## Quick Reference

### Function Selection Guide

| Need to...                       | Use           | Returns                   |
|----------------------------------|---------------|---------------------------|
| Check if pattern at string start | `match()`     | Match or None             |
| Find pattern anywhere            | `search()`    | Match or None             |
| Validate entire string           | `fullmatch()` | Match or None             |
| Get all matches as list          | `findall()`   | List of strings/tuples    |
| Get matches with positions       | `finditer()`  | Iterator of Match objects |
| Replace pattern occurrences      | `sub()`       | Modified string           |
| Replace and count changes        | `subn()`      | (string, count)           |
| Split string by pattern          | `split()`     | List of strings           |
| Reuse pattern multiple times     | `compile()`   | Pattern object            |
| Match literal special chars      | `escape()`    | Escaped string            |

### Common Patterns Quick Reference

See [`regex.md`](./regex.md) for comprehensive regex syntax and [
`regex_python_practical.md`](./regex_python_practical.md) for practical examples.

### Performance Tips

1. **Compile patterns for reuse**:
   ```python
   # GOOD: Compile once
   pattern = re.compile(r'\d+')
   for line in lines:
       pattern.search(line)
   ```

2. **Use raw strings**: Always use `r''` for regex patterns

3. **Be specific**: Avoid overly general patterns like `.*`

4. **Use non-capturing groups**: `(?:...)` when you don't need to capture

---

## Additional Resources

- **Official Documentation**: https://docs.python.org/3/library/re.html
- **General Regex Syntax**: [`regex.md`](./regex.md)
- **Practical Examples**: [`regex_python_practical.md`](./regex_python_practical.md)
- **Testing Tool**: https://regex101.com/ (select Python flavor)
