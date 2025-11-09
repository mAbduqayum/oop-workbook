# Practical Python Regex Examples

Real-world regex patterns and best practices for Python development.

> **Prerequisites**:
> - [`regex.md`](./regex.md) - General regex syntax reference
> - [`regex_python.md`](./regex_python.md) - Python `re` module reference

---

## Table of Contents

1. [Common Validation Patterns](#common-validation-patterns)
2. [Text Processing](#text-processing)
3. [Advanced Patterns](#advanced-patterns)
4. [Performance Best Practices](#performance-best-practices)
5. [Common Pitfalls](#common-pitfalls)
6. [Testing and Debugging](#testing-and-debugging)
7. [When NOT to Use Regex](#when-not-to-use-regex)

---

## Common Validation Patterns

### Email Validation

```python
import re

email_simple = r'^\S+@\S+\.\S+$'
email_standard = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def validate_email(email):
    return bool(re.fullmatch(email_standard, email))

validate_email('user@example.com')           # True
validate_email('user.name+tag@example.co.uk') # True
validate_email('@example.com')                # False
```

**Note**: For production, use the `email-validator` library instead of regex.

### Phone Numbers

```python
us_phone = r'^\+?1?\s*\(?(\d{3})\)?[\s.-]?(\d{3})[\s.-]?(\d{4})$'

def validate_us_phone(phone):
    return bool(re.fullmatch(us_phone, phone))

def extract_phone_parts(phone):
    match = re.match(us_phone, phone)
    if match:
        return match.groups()  # (area_code, prefix, line_number)
    return None

validate_us_phone('(123) 456-7890')  # True
validate_us_phone('123-456-7890')     # True
extract_phone_parts('(555) 123-4567') # ('555', '123', '4567')
```

### URLs

```python
url_basic = r'https?://[^\s]+'
url_complete = r'https?://[\w.-]+(?:\.[\w.-]+)+(?:/[\w._~:/?#@!$&\'()*+,;=-]*)?'

def extract_urls(text):
    return re.findall(url_complete, text)

text = "Visit https://example.com or http://test.org/path?q=1"
extract_urls(text)  # ['https://example.com', 'http://test.org/path?q=1']
```

### Username

```python
username_basic = r'^[a-zA-Z0-9_]{3,16}$'
username_strict = r'^[a-zA-Z][a-zA-Z0-9_-]{2,15}$'

def validate_username(username):
    if not 3 <= len(username) <= 16:
        return False, "Must be 3-16 characters"
    if not re.fullmatch(username_strict, username):
        return False, "Must start with letter, contain only alphanumeric, _, -"
    return True, "Valid"

validate_username('john_doe')    # (True, 'Valid')
validate_username('1john')       # (False, 'Must start with letter...')
```

### Password Strength

```python
password_patterns = {
    'medium': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$',
    'strong': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$',
    'very_strong': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{12,}$'
}

def check_password_strength(password):
    if re.fullmatch(password_patterns['very_strong'], password):
        return "Very Strong"
    elif re.fullmatch(password_patterns['strong'], password):
        return "Strong"
    elif re.fullmatch(password_patterns['medium'], password):
        return "Medium"
    return "Weak"

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("At least 8 characters required")
    if not re.search(r'[a-z]', password):
        errors.append("Must contain lowercase letter")
    if not re.search(r'[A-Z]', password):
        errors.append("Must contain uppercase letter")
    if not re.search(r'\d', password):
        errors.append("Must contain digit")
    if not re.search(r'[@$!%*?&]', password):
        errors.append("Must contain special character")
    return len(errors) == 0, errors

check_password_strength('Pass123!')      # 'Strong'
validate_password('weak')                # (False, [...errors...])
```

### Dates

```python
iso_date = r'^\d{4}-\d{2}-\d{2}$'
us_date = r'^\d{2}/\d{2}/\d{4}$'

def extract_iso_dates(text):
    return re.findall(r'\d{4}-\d{2}-\d{2}', text)

def convert_us_to_iso(date_string):
    return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', date_string)

convert_us_to_iso("12/31/2024")  # '2024-12-31'
```

### IP Address

```python
ipv4_simple = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

ipv4_valid = r'''
    (?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}
    (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
'''

ipv4_pattern = re.compile(ipv4_valid, re.VERBOSE)

def validate_ipv4(ip):
    return bool(ipv4_pattern.fullmatch(ip))

validate_ipv4('192.168.1.1')    # True
validate_ipv4('256.1.1.1')      # False
```

---

## Text Processing

### Log File Parsing

```python
access_log_pattern = r'''
    (?P<ip>\S+)\s+                          # IP address
    \S+\s+                                  # Remote logname
    \S+\s+                                  # Remote user
    \[(?P<datetime>[^\]]+)\]\s+             # Datetime
    "(?P<method>\w+)\s+                     # HTTP method
    (?P<path>\S+)\s+                        # Request path
    (?P<protocol>[^"]+)"\s+                 # Protocol
    (?P<status>\d+)\s+                      # Status code
    (?P<size>\d+)                           # Response size
'''

log_pattern = re.compile(access_log_pattern, re.VERBOSE)

def parse_access_log(line):
    match = log_pattern.search(line)
    return match.groupdict() if match else None

def find_404s(log_file):
    pattern = r'"GET\s+(\S+)\s+HTTP/\d\.\d"\s+404'
    with open(log_file) as f:
        return [match.group(1) for line in f
                if (match := re.search(pattern, line))]
```

### Data Extraction

```python
def extract_currency(text):
    return re.findall(r'\$\d+(?:,\d{3})*(?:\.\d{2})?', text)

def extract_hashtags(text):
    return re.findall(r'#\w+', text)

def extract_mentions(text):
    return re.findall(r'@\w+', text)

def extract_emails(text):
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text)

text = "Price: $1,234.56, Contact: user@example.com #python @john"
extract_currency(text)   # ['$1,234.56']
extract_hashtags(text)   # ['#python']
extract_mentions(text)   # ['@john']
extract_emails(text)     # ['user@example.com']
```

### String Cleaning

```python
def remove_html_tags(html):
    return re.sub(r'<[^>]+>', '', html).strip()

def normalize_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

def remove_urls(text):
    return re.sub(r'https?://\S+', '', text)

def remove_special_chars(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def remove_digits(text):
    return re.sub(r'\d+', '', text)

html = "<p>Hello <b>world</b>!</p>"
remove_html_tags(html)  # 'Hello world!'

normalize_whitespace("hello    world  \n  test")  # 'hello world test'
```

### String Transformation

```python
def convert_date_format(text):
    return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', text)

def anonymize_emails(text):
    return re.sub(r'[\w.-]+@[\w.-]+', '[REDACTED]', text)

def camel_to_snake(name):
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_to_camel(name):
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def capitalize_sentences(text):
    return re.sub(r'(^|[.!?]\s+)([a-z])',
                  lambda m: m.group(1) + m.group(2).upper(),
                  text)

camel_to_snake('getUserName')        # 'get_user_name'
snake_to_camel('get_user_name')      # 'getUserName'
capitalize_sentences("hello. hi!")   # 'Hello. Hi!'
```

### Text Splitting

```python
def split_multi_delim(text, delimiters=r'[,;|]'):
    return re.split(delimiters, text)

def split_flexible(text):
    return re.split(r'[,;|]\s*', text)

def split_on_capitals(text):
    return re.findall(r'[A-Z][a-z]*', text)

def split_paragraphs(text):
    return re.split(r'\n\s*\n', text)

split_multi_delim("apple,banana;cherry|grape")
# ['apple', 'banana', 'cherry', 'grape']

split_on_capitals('GetUserName')
# ['Get', 'User', 'Name']
```

---

## Advanced Patterns

### Lookahead and Lookbehind

```python
def extract_price_value(text):
    return re.findall(r'(?<=\$)\d+\.\d{2}', text)

def find_non_pixel_numbers(css):
    return re.findall(r'\d+(?!px)', css)

def word_before(text, target):
    pattern = rf'\b(\w+)\s+(?={target}\b)'
    return re.findall(pattern, text)

def word_after(text, target):
    pattern = rf'(?<={target}\s)\w+'
    return re.findall(pattern, text)

extract_price_value("Price: $25.99")     # ['25.99']
css = "width: 100px; height: 50"
find_non_pixel_numbers(css)              # ['50']

text = "the quick brown fox"
word_before(text, 'fox')                 # ['brown']
word_after(text, 'brown')                # ['fox']
```

### Word Boundaries

```python
def replace_whole_word(text, old, new):
    pattern = rf'\b{re.escape(old)}\b'
    return re.sub(pattern, new, text)

def find_standalone_numbers(text):
    return re.findall(r'\b\d+\b', text)

text = "cat category caterpillar"
replace_whole_word(text, 'cat', 'dog')  # 'dog category caterpillar'

text = "I have 3 cats and item123"
find_standalone_numbers(text)            # ['3']
```

### Named Groups

```python
log_pattern = r'''
    (?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s+
    \[(?P<level>\w+)\]\s+
    (?P<message>.+)
'''

def parse_log_entry(line):
    match = re.search(log_pattern, line, re.VERBOSE)
    return match.groupdict() if match else None

log = "2024-01-15 10:30:45 [ERROR] Connection failed"
parse_log_entry(log)
# {'timestamp': '2024-01-15 10:30:45', 'level': 'ERROR',
#  'message': 'Connection failed'}
```

### Backreferences

```python
def find_doubled_words(text):
    return re.findall(r'\b(\w+)\s+\1\b', text)

def remove_doubled_words(text):
    return re.sub(r'\b(\w+)\s+\1\b', r'\1', text)

def find_repeated_chars(text):
    return re.findall(r'(.)\1+', text)

def extract_quoted_content(text):
    pattern = r'''(?P<quote>['"])(.*?)(?P=quote)'''
    matches = re.findall(pattern, text)
    return [content for quote, content in matches]

find_doubled_words("the the quick")      # ['the']
remove_doubled_words("the the quick")    # 'the quick'
extract_quoted_content('He said "hi"')   # ['hi']
```

---

## Performance Best Practices

### Compile Patterns for Reuse

```python
# BAD: Compiles on every iteration
def process_lines_bad(lines):
    return [line for line in lines if re.search(r'\d{3}-\d{3}-\d{4}', line)]

# GOOD: Compile once
def process_lines_good(lines):
    phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    return [line for line in lines if phone_pattern.search(line)]

# BEST: Use filter
def process_lines_best(lines):
    phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    return list(filter(phone_pattern.search, lines))
```

### Use Non-Capturing Groups

```python
# BAD: Unnecessary capturing
url_bad = r'(https?|ftp)://\S+'

# GOOD: Non-capturing group
url_good = r'(?:https?|ftp)://\S+'

# Only capture what you need
domain_pattern = r'(?:https?://)?([a-z0-9.-]+\.[a-z]{2,})'
```

### Avoid Backtracking

```python
# BAD: Too general, causes backtracking
email_bad = r'.*@.*'

# GOOD: More specific
email_good = r'\S+@\S+'

# BAD: Nested quantifiers (catastrophic backtracking)
dangerous = r'(a+)+'

# GOOD: Specific repetition
safe = r'a{1,100}'

# BAD: Greedy with complex pattern
html_bad = r'<div>.*</div>'

# GOOD: Non-greedy
html_good = r'<div>.*?</div>'
```

### Use Appropriate Functions

```python
# For simple substring checks
# BAD
if re.search(r'hello', text):
    pass

# GOOD
if 'hello' in text:
    pass

# For simple replacements
# BAD
text = re.sub(r' ', '_', text)

# GOOD
text = text.replace(' ', '_')

# Use finditer() for large texts with positions
# BAD: findall() when you need positions
matches = re.findall(pattern, large_text)

# GOOD: finditer() for memory efficiency
for match in re.finditer(pattern, large_text):
    print(f"{match.group()} at {match.start()}")
```

---

## Common Pitfalls

### The Backslash Problem

```python
# WRONG: Single backslash
pattern = '\d+'  # Interpreted as '\\d+'

# RIGHT: Use raw strings
pattern = r'\d+'

# Escaping backslashes in paths
# WRONG
file_pattern = '\\w+\\.txt'

# RIGHT
file_pattern = r'\w+\.txt'
```

### Greedy vs Non-Greedy

```python
html = '<div>Hello</div><div>World</div>'

# GREEDY: Matches as much as possible
greedy = re.findall(r'<div>.*</div>', html)
# ['<div>Hello</div><div>World</div>']

# NON-GREEDY: Matches as little as possible
non_greedy = re.findall(r'<div>.*?</div>', html)
# ['<div>Hello</div>', '<div>World</div>']

text = 'Say "hello" and "goodbye"'

re.findall(r'".*"', text)    # ['"hello" and "goodbye"']
re.findall(r'".*?"', text)   # ['"hello"', '"goodbye"']
```

### Multiline and DOTALL

```python
text = "line1\nline2\nline3"

# Without MULTILINE
re.findall(r'^line', text)        # ['line1']

# With MULTILINE
re.findall(r'^line', text, re.M)  # ['line1', 'line2', 'line3']

# Without DOTALL: . doesn't match newline
print(re.search(r'line1.*line3', text))  # None

# With DOTALL: . matches newline
re.search(r'line1.*line3', text, re.S)   # Match!
```

### Empty Matches

```python
text = 'abc'

# Empty pattern matches at every position
re.sub(r'', '-', text)       # '-a-b-c-'

# Optional patterns can match empty
pattern = r'\d*'
re.findall(pattern, 'a1b2c')  # ['', '1', '', '2', '', '']

# Use + instead of * for at least one match
pattern = r'\d+'
re.findall(pattern, 'a1b2c')  # ['1', '2']
```

---

## Testing and Debugging

### Use Verbose Mode

```python
# Hard to read
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

# Clear with VERBOSE
password_pattern = re.compile(r'''
    ^                           # Start
    (?=.*[a-z])                 # At least one lowercase
    (?=.*[A-Z])                 # At least one uppercase
    (?=.*\d)                    # At least one digit
    (?=.*[@$!%*?&])             # At least one special char
    [A-Za-z\d@$!%*?&]{8,}       # At least 8 from allowed set
    $                           # End
''', re.VERBOSE)
```

### Test with Edge Cases

```python
def test_email_validation():
    test_cases = [
        ('user@example.com', True, 'Basic email'),
        ('user.name@example.com', True, 'Dot in username'),
        ('user+tag@example.com', True, 'Plus in username'),
        ('user@sub.example.com', True, 'Subdomain'),
        ('@example.com', False, 'Missing username'),
        ('user@', False, 'Missing domain'),
        ('user', False, 'No @ symbol'),
        ('user@domain', False, 'No TLD'),
        ('user name@example.com', False, 'Space in username'),
    ]

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    for email, should_match, description in test_cases:
        match = re.fullmatch(email_pattern, email)
        actual = match is not None
        status = '✓' if actual == should_match else '✗'
        print(f"{status} {description}: {email}")
        assert actual == should_match, f"Failed: {description}"
```

### Use re.DEBUG

```python
# See how Python compiles your pattern
pattern = re.compile(r'\d+', re.DEBUG)

# Verify metacharacter interpretation
re.search('x[123]{2,4}y', 'x222y', re.DEBUG)
# Shows: MAX_REPEAT 2 4 ...

# Verify literal interpretation
re.search('x[123]{foo}y', 'x{foo}y', re.DEBUG)
# Shows: LITERAL 123, LITERAL 102... (no MAX_REPEAT)
```

---

## When NOT to Use Regex

### Use String Methods Instead

```python
# Checking substring
if re.search(r'hello', text):  # BAD
if 'hello' in text:            # GOOD

# Checking start/end
if re.match(r'Hello', text):   # BAD
if text.startswith('Hello'):   # GOOD

# Simple replacement
text = re.sub(r' ', '_', text) # BAD
text = text.replace(' ', '_')  # GOOD

# Case-insensitive comparison
if re.search(r'(?i)hello', text):  # BAD
if 'hello' in text.lower():        # GOOD
```

### Use Specialized Libraries

```python
# Email validation
from email_validator import validate_email, EmailNotValidError

try:
    valid = validate_email(email_address)
    email = valid.email
except EmailNotValidError as e:
    print(str(e))

# HTML/XML parsing
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

# URL parsing
from urllib.parse import urlparse
url = urlparse('https://example.com/path?query=1')
print(url.scheme, url.netloc, url.path)

# Date parsing
from datetime import datetime
date = datetime.strptime('2024-01-15', '%Y-%m-%d')

# Or use dateutil
from dateutil import parser
date = parser.parse('Jan 15, 2024')

# CSV parsing
import csv
with open('file.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### Complex Grammars

```python
# For complex grammars, use a parser library
# - pyparsing: custom parsers
# - lark: grammar-based parsing
# - PLY: Python Lex-Yacc
# - textX: DSL creation

from pyparsing import Word, alphas, nums, oneOf

variable = Word(alphas, alphas + nums)
operator = oneOf('+ - * /')
expression = variable + operator + variable

result = expression.parseString('x + y')
```

---

## Summary

**Key Takeaways:**

1. **Always use raw strings** (`r""`) for regex patterns
2. **Compile patterns** when reusing them
3. **Be specific** to avoid backtracking
4. **Use non-capturing groups** `(?:...)` when not capturing
5. **Test edge cases** thoroughly
6. **Consider alternatives** - regex isn't always the best tool
7. **Use VERBOSE mode** for complex patterns
8. **Know when NOT to use regex** - string methods are often better

**Performance Hierarchy** (fastest → slowest):
1. String methods (`in`, `startswith`, `replace`)
2. Compiled regex patterns
3. Non-compiled regex
4. Complex regex with backtracking

**Resource Hierarchy** (simplest → most powerful):
1. String methods
2. Standard `re` module
3. `regex` module (more features)
4. Specialized libraries (email-validator, BeautifulSoup, etc.)
5. Parser libraries (pyparsing, lark, PLY)

**Online Testing Tools:**
- **regex101.com** - Best overall, select "Python" flavor
- **pythex.org** - Python-specific tester
- **regexr.com** - Visual explanations
- **debuggex.com** - Railroad diagrams

For more information:
- [General regex syntax](./regex.md)
- [Python re module reference](./regex_python.md)
- [Official Python documentation](https://docs.python.org/3/library/re.html)
