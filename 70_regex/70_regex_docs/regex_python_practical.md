# Practical Python Regex Examples

Real-world regex patterns and best practices for Python development.

> **Prerequisites**:
> - [`regex.md`](./regex.md) - General regex syntax reference
> - [`regex_python.md`](./regex_python.md) - Python `re` module reference

---

## Table of Contents

1. [Common Validation Patterns](#common-validation-patterns)
2. [Text Processing Examples](#text-processing-examples)
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

# Simple validation (basic structure check)
simple_email = r'^\S+@\S+\.\S+$'

# Standard validation (more robust)
standard_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


# Usage
def validate_email(email):
    return bool(re.fullmatch(standard_email, email))


# Tests
validate_email('user@example.com')  # True
validate_email('user.name+tag@example.co.uk')  # True
validate_email('@example.com')  # False
validate_email('user@')  # False
```

**Note**: Perfect email validation with regex is nearly impossible (RFC 5322 is complex). For production, consider using
the `email-validator` library.

### Phone Number Validation

```python
# US phone number (various formats)
us_phone = r'^\+?1?\s*\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'


# Matches:
# (123) 456-7890
# 123-456-7890
# 1234567890
# +1-123-456-7890
# +1 (123) 456-7890

def validate_us_phone(phone):
    return bool(re.fullmatch(us_phone, phone))


# Strict format: XXX-XXX-XXXX
strict_phone = r'^\d{3}-\d{3}-\d{4}$'

# International phone (E.164 format)
international_phone = r'^\+?[1-9][0-9]{7,14}$'
```

### URL Validation

```python
# Basic URL (http/https)
basic_url = r'https?://[^\s]+'

# More complete URL
complete_url = r'https?://[\w.-]+(?:\.[\w.-]+)+(?:/[\w._~:/?#@!$&\'()*+,;=-]*)?'

# With optional protocol
flexible_url = r'(?:https?://)?[\w.-]+(?:\.[\w.-]+)+(?:/[\w._~:/?#@!$&\'()*+,;=-]*)?'


# Usage
def extract_urls(text):
    return re.findall(complete_url, text)


text = "Visit https://example.com or http://test.org/path?query=1"
extract_urls(text)
# ['https://example.com', 'http://test.org/path?query=1']
```

### Username Validation

```python
# Alphanumeric with underscore, 3-16 characters
username_basic = r'^[a-zA-Z0-9_]{3,16}$'

# Must start with letter, 3-16 characters
username_strict = r'^[a-zA-Z][a-zA-Z0-9_-]{2,15}$'

# No consecutive special characters
username_advanced = r'^[a-zA-Z0-9](?:[a-zA-Z0-9_-]*[a-zA-Z0-9])?{2,14}$'


def validate_username(username):
    if not re.fullmatch(username_strict, username):
        return False, "Invalid format"
    if len(username) < 3:
        return False, "Too short"
    if len(username) > 16:
        return False, "Too long"
    return True, "Valid"
```

### Password Strength Validation

```python
# At least 8 characters, one uppercase, one lowercase, one digit
password_medium = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'

# Strong: add special character requirement
password_strong = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

# Very strong: 12+ chars, all requirements
password_very_strong = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{12,}$'


def check_password_strength(password):
    if re.fullmatch(password_very_strong, password):
        return "Very Strong"
    elif re.fullmatch(password_strong, password):
        return "Strong"
    elif re.fullmatch(password_medium, password):
        return "Medium"
    else:
        return "Weak"


# Detailed validation
def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Must be at least 8 characters")
    if not re.search(r'[a-z]', password):
        errors.append("Must contain lowercase letter")
    if not re.search(r'[A-Z]', password):
        errors.append("Must contain uppercase letter")
    if not re.search(r'\d', password):
        errors.append("Must contain digit")
    if not re.search(r'[@$!%*?&]', password):
        errors.append("Must contain special character")

    return len(errors) == 0, errors
```

### Date Validation

```python
# ISO format: YYYY-MM-DD
iso_date = r'^\d{4}-\d{2}-\d{2}$'

# US format: MM/DD/YYYY
us_date = r'^\d{2}/\d{2}/\d{4}$'

# European format: DD.MM.YYYY
eu_date = r'^\d{2}\.\d{2}\.\d{4}$'

# Flexible date (multiple formats)
flexible_date = r'\d{1,4}[-/.]\d{1,2}[-/.]\d{1,4}'


# Extract and convert dates
def extract_iso_dates(text):
    return re.findall(r'\d{4}-\d{2}-\d{2}', text)


# Convert US to ISO format
def convert_us_to_iso(date_string):
    return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', date_string)


convert_us_to_iso("12/31/2024")  # '2024-12-31'
```

### IP Address Validation

```python
# Basic IPv4 (no range validation)
basic_ipv4 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# Valid IPv4 with range validation (0-255)
valid_ipv4 = r'''
    (?:
        (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.
    ){3}
    (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
'''

# Compile with VERBOSE flag for readability
ipv4_pattern = re.compile(valid_ipv4, re.VERBOSE)


# Usage
def validate_ipv4(ip):
    return bool(ipv4_pattern.fullmatch(ip))


validate_ipv4('192.168.1.1')  # True
validate_ipv4('255.255.255.255')  # True
validate_ipv4('256.1.1.1')  # False
```

---

## Text Processing Examples

### Log File Parsing

```python
# Apache/Nginx access log format
# 192.168.1.1 - - [10/Oct/2024:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 1234

access_log_pattern = r'''
    (?P<ip>\S+)\s+                          # IP address
    \S+\s+                                  # Remote logname (usually -)
    \S+\s+                                  # Remote user (usually -)
    \[(?P<datetime>[^\]]+)\]\s+             # Datetime
    "(?P<method>\w+)\s+                     # HTTP method
    (?P<path>\S+)\s+                        # Request path
    (?P<protocol>[^"]+)"\s+                 # Protocol
    (?P<status>\d+)\s+                      # Status code
    (?P<size>\d+)                           # Response size
'''

log_pattern = re.compile(access_log_pattern, re.VERBOSE)


# Parse log line
def parse_access_log(line):
    match = log_pattern.search(line)
    if match:
        return match.groupdict()
    return None


# Extract error messages from logs
def extract_errors(log_file):
    error_pattern = r'\[ERROR\]\s+(.+?)(?=\[|$)'
    with open(log_file) as f:
        for line in f:
            errors = re.findall(error_pattern, line)
            if errors:
                yield errors[0]


# Find all 404 errors
def find_404s(log_file):
    pattern = r'"GET\s+(\S+)\s+HTTP/\d\.\d"\s+404'
    with open(log_file) as f:
        return [match.group(1) for line in f
                for match in [re.search(pattern, line)] if match]
```

### Data Extraction

```python
# Extract dates (multiple formats)
def extract_dates(text):
    # ISO format: YYYY-MM-DD
    iso_dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)

    # US format: MM/DD/YYYY
    us_dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)

    return iso_dates + us_dates


# Extract currency amounts
def extract_prices(text):
    # Matches: $1,234.56, $99.99, $1000
    pattern = r'\$\d+(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)


text = "Price: $1,234.56, Tax: $99.99, Total: $1,334.55"
extract_prices(text)  # ['$1,234.56', '$99.99', '$1,334.55']


# Extract hashtags
def extract_hashtags(text):
    return re.findall(r'#\w+', text)


# Extract @mentions
def extract_mentions(text):
    return re.findall(r'@\w+', text)


tweet = "Hello @alice! Check out #python #regex #coding"
extract_mentions(tweet)  # ['@alice']
extract_hashtags(tweet)  # ['#python', '#regex', '#coding']


# Extract email addresses
def extract_emails(text):
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text)


# Extract phone numbers (US format)
def extract_phones(text):
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(pattern, text)
```

### String Cleaning

```python
# Remove HTML tags
def remove_html_tags(html):
    clean = re.sub(r'<[^>]+>', '', html)
    return clean.strip()


html = "<p>Hello <b>world</b>!</p>"
remove_html_tags(html)  # 'Hello world!'


# Remove extra whitespace
def normalize_whitespace(text):
    # Replace multiple spaces with single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


normalize_whitespace("hello    world  \n\n  test")  # 'hello world test'


# Remove URLs from text
def remove_urls(text):
    return re.sub(r'https?://\S+', '', text)


# Remove email addresses
def remove_emails(text):
    return re.sub(r'\S+@\S+', '', text)


# Remove special characters (keep alphanumeric and spaces)
def remove_special_chars(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)


# Remove digits
def remove_digits(text):
    return re.sub(r'\d+', '', text)


# Remove punctuation but keep sentence structure
def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)
```

### Find and Replace

```python
# Convert dates from MM/DD/YYYY to YYYY-MM-DD
def convert_date_format(text):
    return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', text)


text = "Date: 12/31/2024"
convert_date_format(text)  # 'Date: 2024-12-31'


# Anonymize email addresses
def anonymize_emails(text):
    return re.sub(r'[\w.-]+@[\w.-]+', '[EMAIL REDACTED]', text)


# Anonymize phone numbers
def anonymize_phones(text):
    return re.sub(r'\d{3}-\d{3}-\d{4}', 'XXX-XXX-XXXX', text)


# Convert camelCase to snake_case
def camel_to_snake(name):
    # Insert underscore before uppercase letters
    s1 = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Insert underscore before uppercase in acronyms
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


camel_to_snake('getUserName')  # 'get_user_name'
camel_to_snake('HTTPResponse')  # 'http_response'


# Convert snake_case to camelCase
def snake_to_camel(name):
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


snake_to_camel('get_user_name')  # 'getUserName'


# Capitalize sentences
def capitalize_sentences(text):
    return re.sub(r'(^|[.!?]\s+)([a-z])',
                  lambda m: m.group(1) + m.group(2).upper(),
                  text)


text = "hello world. how are you? fine thanks!"
capitalize_sentences(text)  # 'Hello world. How are you? Fine thanks!'
```

### Text Splitting

```python
# Split by multiple delimiters
def split_multi_delim(text):
    # Split by comma, semicolon, or pipe
    return re.split(r'[,;|]', text)


text = "apple,banana;cherry|grape"
split_multi_delim(text)  # ['apple', 'banana', 'cherry', 'grape']


# Split by delimiter with optional whitespace
def split_flexible(text):
    return re.split(r'[,;|]\s*', text)


text = "apple, banana ; cherry| grape"
split_flexible(text)  # ['apple', 'banana', 'cherry', 'grape']


# Split on capital letters (for camelCase)
def split_on_capitals(text):
    return re.findall(r'[A-Z][a-z]*', text)


split_on_capitals('GetUserNameFromDatabase')


# ['Get', 'User', 'Name', 'From', 'Database']

# Split paragraphs
def split_paragraphs(text):
    return re.split(r'\n\s*\n', text)
```

---

## Advanced Patterns

### Lookahead and Lookbehind

```python
# Extract price without currency symbol
def extract_price_value(text):
    # Positive lookbehind: match digits after $
    pattern = r'(?<=\$)\d+\.\d{2}'
    return re.findall(pattern, text)


text = "Price: $25.99"
extract_price_value(text)  # ['25.99']


# Find numbers NOT followed by 'px'
def find_non_pixel_numbers(css):
    # Negative lookahead: match numbers not followed by px
    pattern = r'\d+(?!px)'
    return re.findall(pattern, css)


css = "width: 100px; height: 50; margin: 10px"
find_non_pixel_numbers(css)  # ['50']

# Password validation using lookahead
password_with_lookahead = r'''
    ^                       # Start
    (?=.*[a-z])             # Must contain lowercase
    (?=.*[A-Z])             # Must contain uppercase
    (?=.*\d)                # Must contain digit
    (?=.*[@$!%*?&])         # Must contain special char
    [A-Za-z\d@$!%*?&]{8,}   # At least 8 chars from allowed set
    $                       # End
'''


# Extract word before specific word
def word_before(text, target):
    pattern = rf'\b(\w+)\s+(?={target}\b)'
    return re.findall(pattern, text)


text = "the quick brown fox jumps"
word_before(text, 'fox')  # ['brown']


# Extract word after specific word
def word_after(text, target):
    pattern = rf'(?<={target}\s)\w+'
    return re.findall(pattern, text)


word_after(text, 'brown')  # ['fox']
```

### Word Boundaries

```python
# Match whole word only
def replace_whole_word(text, old, new):
    pattern = rf'\b{re.escape(old)}\b'
    return re.sub(pattern, new, text)


text = "cat category caterpillar"
replace_whole_word(text, 'cat', 'dog')  # 'dog category caterpillar'


# Find standalone numbers
def find_standalone_numbers(text):
    return re.findall(r'\b\d+\b', text)


text = "I have 3 cats and 10 dogs, plus item123"
find_standalone_numbers(text)  # ['3', '10']


# British to American spelling
def british_to_american(text):
    # Replace 'colour' with 'color', 'honour' with 'honor', etc.
    return re.sub(r'\b(\w+)our\b', r'\1or', text)


british_to_american("The colour and honour are important")
# 'The color and honor are important'
```

### Named Groups

```python
# Parse structured data
log_pattern = r'''
    (?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s+
    \[(?P<level>\w+)\]\s+
    (?P<message>.+)
'''

log_regex = re.compile(log_pattern, re.VERBOSE)


def parse_log_entry(line):
    match = log_regex.search(line)
    if match:
        return match.groupdict()
    return None


log = "2024-01-15 10:30:45 [ERROR] Database connection failed"
parse_log_entry(log)
# {'timestamp': '2024-01-15 10:30:45', 'level': 'ERROR',
#  'message': 'Database connection failed'}

# Extract structured contact info
contact_pattern = r'''
    (?P<name>[A-Z][a-z]+\s[A-Z][a-z]+)\s*
    (?P<email>\S+@\S+)\s*
    (?P<phone>\d{3}-\d{3}-\d{4})
'''


def parse_contact(text):
    match = re.search(contact_pattern, text, re.VERBOSE)
    if match:
        return match.groupdict()
    return None
```

### Backreferences

```python
# Find doubled words
def find_doubled_words(text):
    pattern = r'\b(\w+)\s+\1\b'
    return re.findall(pattern, text)


text = "The the quick brown brown fox"
find_doubled_words(text)  # ['The', 'brown']


# Remove doubled words
def remove_doubled_words(text):
    pattern = r'\b(\w+)\s+\1\b'
    return re.sub(pattern, r'\1', text)


remove_doubled_words(text)  # 'The quick brown fox'


# Find repeated characters
def find_repeated_chars(text):
    # Find any character repeated 2+ times
    pattern = r'(.)\1+'
    return re.findall(pattern, text)


find_repeated_chars("hello goood")  # ['l', 'o']


# Match matching quotes
def extract_quoted_strings(text):
    # Named backreference for matching quotes
    pattern = r'''(?P<quote>['"]).*?(?P=quote)'''
    return re.findall(pattern, text, re.VERBOSE)


text = '''He said "hello" and she said 'goodbye' '''
extract_quoted_strings(text)  # ['"', "'"]


# Better version returning content
def extract_quoted_content(text):
    pattern = r'''(?P<quote>['"])(.*?)(?P=quote)'''
    matches = re.findall(pattern, text, re.VERBOSE)
    return [content for quote, content in matches]


extract_quoted_content(text)  # ['hello', 'goodbye']


# Find palindromes (simplified)
def is_palindrome_pattern(text):
    # Simple palindrome check for 3-7 letter words
    pattern = r'\b(\w)(\w)(\w)?\3\2\1\b'
    return bool(re.search(pattern, text))
```

---

## Performance Best Practices

### Compile Patterns for Reuse

```python
# BAD: Compiles pattern on every iteration
def process_lines_bad(lines):
    results = []
    for line in lines:
        if re.search(r'\d{3}-\d{3}-\d{4}', line):
            results.append(line)
    return results


# GOOD: Compile once, reuse many times
def process_lines_good(lines):
    phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    results = []
    for line in lines:
        if phone_pattern.search(line):
            results.append(line)
    return results


# EVEN BETTER: Use filter with compiled pattern
def process_lines_better(lines):
    phone_pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    return list(filter(phone_pattern.search, lines))
```

### Use Non-Capturing Groups

```python
# When you don't need to capture, use (?:...)

# BAD: Unnecessary capturing group
url_pattern = r'(https?|ftp)://\S+'

# GOOD: Non-capturing group
url_pattern = r'(?:https?|ftp)://\S+'

# Example with multiple groups
# Only capture domain, not protocol
domain_pattern = r'(?:https?://)?([a-z0-9.-]+\.[a-z]{2,})'
```

### Be Specific and Avoid Backtracking

```python
# BAD: Too general, causes backtracking
email_bad = r'.*@.*'

# GOOD: More specific
email_good = r'\S+@\S+'

# BAD: Nested quantifiers (catastrophic backtracking)
dangerous = r'(a+)+'

# GOOD: Be specific about repetition
safe = r'a{1,100}'

# BAD: Greedy quantifier with complex pattern
html_bad = r'<div>.*</div>'  # Can match across multiple divs

# GOOD: Non-greedy quantifier
html_good = r'<div>.*?</div>'
```

### Use Appropriate Functions

```python
# For simple substring checks, use string methods
# BAD
if re.search(r'hello', text):
    pass

# GOOD
if 'hello' in text:
    pass

# For simple replacements, use str.replace()
# BAD
text = re.sub(r' ', '_', text)

# GOOD
text = text.replace(' ', '_')

# For finding all matches without positions, use findall()
# For finding with positions or large text, use finditer()

# BAD: findall() for large text when you need positions
matches = re.findall(pattern, large_text)
for match in matches:
# Can't access position info

# GOOD: finditer() for memory efficiency and position info
for match in re.finditer(pattern, large_text):
    print(f"{match.group()} at {match.start()}")
```

### Limit Backtracking with Atomic Groups

Note: Atomic groups `(?>...)` are not available in Python's standard `re` module. Use the `regex` library instead.

```python
# Requires: pip install regex
import regex

# Atomic group prevents backtracking within the group
pattern = regex.compile(r'(?>a+)b')

# Without atomic group, this could hang
# With atomic group, fails fast
```

---

## Common Pitfalls

### The Backslash Problem

```python
# WRONG: Single backslash in regular string
pattern = '\d+'  # Actually becomes '\\d+' (literal \d+)

# RIGHT: Use raw strings
pattern = r'\d+'  # Stays as '\d+' (regex for digits)

# Alternative: Double-escape (not recommended)
pattern = '\\d+'  # Works but harder to maintain

# Real-world example
# WRONG
file_pattern = '\\w+\\.txt'  # Hard to read

# RIGHT
file_pattern = r'\w+\.txt'  # Clear and correct

# When raw strings don't work (rare)
# If you need actual backslash-n (not newline):
pattern = r'\\n'  # Matches literal \n in text
```

### Greedy vs Non-Greedy Quantifiers

```python
html = '<div>Hello</div><div>World</div>'

# GREEDY: Matches as much as possible
greedy = re.findall(r'<div>.*</div>', html)
# ['<div>Hello</div><div>World</div>']  # Matches across both!

# NON-GREEDY: Matches as little as possible
non_greedy = re.findall(r'<div>.*?</div>', html)
# ['<div>Hello</div>', '<div>World</div>']  # Separate matches

# Another example
text = 'Say "hello" and "goodbye"'

# Greedy
re.findall(r'".*"', text)
# ['"hello" and "goodbye"']  # Matches entire string

# Non-greedy
re.findall(r'".*?"', text)
# ['"hello"', '"goodbye"']  # Separate quotes
```

### Multiline and DOTALL Flags

```python
text = "line1\nline2\nline3"

# Without MULTILINE: ^ and $ match string start/end
re.findall(r'^line', text)
# ['line1']  # Only matches start of entire string

# With MULTILINE: ^ and $ match line boundaries
re.findall(r'^line', text, re.M)
# ['line1', 'line2', 'line3']  # Matches start of each line

# Without DOTALL: . doesn't match newlines
re.search(r'line1.*line3', text)
# None  # . doesn't match \n

# With DOTALL: . matches newlines
re.search(r'line1.*line3', text, re.S)
# Matches!

# Real example: Extract multi-line code blocks
markdown = """
```python
def hello():
    print("hi")
```

"""

# Without DOTALL - won't work

re.findall(r'```python(.*)```', markdown)  # []

# With DOTALL - works

re.findall(r'```python(.*?)```', markdown, re.S)  # ['\ndef hello():\n    print("hi")\n']

```

### Empty Matches

```python
# Empty matches create interesting behavior
text = 'abc'

# Empty pattern matches at every position
re.sub(r'', '-', text)
# '-a-b-c-'  # Inserts at every position

# Empty matches in split
re.split(r'', 'abc')
# ['', 'a', 'b', 'c', '']  # Splits at every position

# Be careful with optional patterns
pattern = r'\d*'  # Can match empty string!
re.findall(pattern, 'a1b2c')
# ['', '1', '', '2', '', '']  # Includes empty matches

# Fix: Use + instead of * if you want at least one
pattern = r'\d+'
re.findall(pattern, 'a1b2c')
# ['1', '2']  # Only non-empty matches
```

### Group Numbering

```python
# Groups are numbered left-to-right by opening parenthesis
pattern = r'((a)(b))(c)'
#         1  2  3   4

match = re.search(pattern, 'abc')
match.group(1)  # 'ab'
match.group(2)  # 'a'
match.group(3)  # 'b'
match.group(4)  # 'c'

# Non-capturing groups don't get numbers
pattern = r'(?:a)(b)'
#          non  1

match = re.search(pattern, 'ab')
match.group(1)  # 'b'
match.group(2)  # Error: no group 2
```

---

## Testing and Debugging

### Use re.DEBUG Flag

```python
# See how Python compiles your pattern
pattern = re.compile(r'\d+', re.DEBUG)

# Outputs compilation info:
# LITERAL 92
# LITERAL 100
# MAX_REPEAT 1 MAXREPEAT
#   ...
```

### Test with Edge Cases

```python
def test_email_validation():
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    test_cases = [
        # (input, should_match, description)
        ('user@example.com', True, 'Basic email'),
        ('user.name@example.com', True, 'Dot in username'),
        ('user+tag@example.com', True, 'Plus in username'),
        ('user@subdomain.example.com', True, 'Subdomain'),
        ('@example.com', False, 'Missing username'),
        ('user@', False, 'Missing domain'),
        ('user', False, 'No @ symbol'),
        ('user@domain', False, 'No TLD'),
        ('user name@example.com', False, 'Space in username'),
    ]

    for email, should_match, description in test_cases:
        match = re.fullmatch(email_pattern, email)
        actual = match is not None
        status = '✓' if actual == should_match else '✗'
        print(f"{status} {description}: {email} -> {actual}")
        assert actual == should_match, f"Failed: {description}"


test_email_validation()
```

### Use Verbose Mode for Complex Patterns

```python
# Hard to read
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

# Much clearer with VERBOSE flag
password_pattern = re.compile(r'''
    ^                           # Start of string
    (?=.*[a-z])                 # At least one lowercase letter
    (?=.*[A-Z])                 # At least one uppercase letter
    (?=.*\d)                    # At least one digit
    (?=.*[@$!%*?&])             # At least one special character
    [A-Za-z\d@$!%*?&]{8,}       # At least 8 characters from allowed set
    $                           # End of string
''', re.VERBOSE)

# Note: In VERBOSE mode, whitespace is ignored (use \s to match actual space)
# Comments start with #
```

### Interactive Testing

```python
# Quick interactive regex tester
def regex_tester():
    while True:
        pattern = input("Enter pattern (or 'quit'): ")
        if pattern.lower() == 'quit':
            break

        try:
            compiled = re.compile(pattern)
        except re.error as e:
            print(f"Invalid pattern: {e}")
            continue

        text = input("Enter text to match: ")

        matches = compiled.findall(text)
        print(f"Matches: {matches}")

        match = compiled.search(text)
        if match:
            print(f"First match: '{match.group()}' at position {match.start()}-{match.end()}")
        else:
            print("No matches found")

# Or use online tools:
# - regex101.com (select Python flavor)
# - regexr.com
# - pythex.org
```

---

## When NOT to Use Regex

### Use String Methods Instead

```python
# Checking substring existence
# BAD
if re.search(r'hello', text):
    pass

# GOOD
if 'hello' in text:
    pass

# Checking string start/end
# BAD
if re.match(r'Hello', text):
    pass

# GOOD
if text.startswith('Hello'):
    pass

# Simple replacement
# BAD
text = re.sub(r' ', '_', text)

# GOOD
text = text.replace(' ', '_')

# Case-insensitive comparison
# BAD
if re.search(r'(?i)hello', text):
    pass

# GOOD
if 'hello' in text.lower():
    pass
```

### Use Specialized Libraries

```python
# Email validation
# Instead of complex regex, use:
# pip install email-validator
from email_validator import validate_email, EmailNotValidError

try:
    valid = validate_email(email_address)
    email = valid.email  # normalized form
except EmailNotValidError as e:
    print(str(e))

# HTML/XML parsing
# Instead of regex, use:
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all('a')

# URL parsing
# Instead of regex, use:
from urllib.parse import urlparse

url = urlparse('https://example.com/path?query=1')
print(url.scheme, url.netloc, url.path)

# Date parsing
# Instead of regex, use:
from datetime import datetime

date = datetime.strptime('2024-01-15', '%Y-%m-%d')

# Or for flexible parsing:
# pip install python-dateutil
from dateutil import parser

date = parser.parse('Jan 15, 2024')

# CSV parsing
# Instead of regex, use:
import csv

with open('file.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# JSON parsing
# Instead of regex, use:
import json

data = json.loads(json_string)
```

### Complex Pattern Matching

```python
# For complex grammars, use a parser library
# Instead of nested regex, use:

# pyparsing - for creating custom parsers
# lark - for grammar-based parsing
# PLY - Python Lex-Yacc
# textX - for DSL creation

# Example: parsing a simple expression
from pyparsing import Word, alphas, nums, oneOf

# Define grammar
variable = Word(alphas, alphas + nums)
operator = oneOf('+ - * /')
expression = variable + operator + variable

# Parse
result = expression.parseString('x + y')
```

---

## Alternative Tools and Libraries

### The `regex` Module (More Features)

```python
# pip install regex
import regex

# Supports features not in `re`:
# - Recursive patterns
# - Variable-length lookbehinds
# - More Unicode support
# - Fuzzy matching
# - Better performance in some cases

# Variable-length lookbehind (not possible in re)
pattern = regex.compile(r'(?<=\w{2,5})ing')

# Fuzzy matching
pattern = regex.compile(r'(hello){e<=2}')  # Allow up to 2 errors
pattern.findall('helo heelo helllo')  # Matches with errors
```

### Performance Alternatives

```python
# For matching many keywords, use Aho-Corasick
# pip install pyahocorasick
import ahocorasick

A = ahocorasick.Automaton()
for keyword in ['apple', 'banana', 'cherry']:
    A.add_word(keyword, keyword)
A.make_automaton()

# Much faster than regex for 1000+ keywords
for end_index, keyword in A.iter(text):
    print(f"Found {keyword}")
```

### Online Testing Tools

- **regex101.com** - Best overall, select "Python" flavor
- **pythex.org** - Python-specific regex tester
- **regexr.com** - Visual explanation of patterns
- **debuggex.com** - Visual railroad diagrams
- **txt2re.com** - Generate regex from examples

---

## Summary

**Key Takeaways:**

1. **Always use raw strings** (`r""`) for regex patterns
2. **Compile patterns** when reusing them
3. **Be specific** to avoid backtracking issues
4. **Use non-capturing groups** `(?:...)` when you don't need to capture
5. **Test edge cases** thoroughly
6. **Consider alternatives** - regex isn't always the best tool
7. **Use VERBOSE mode** for complex patterns
8. **Know when NOT to use regex** - simple string methods are often better

**Performance Hierarchy (fastest to slowest):**

1. String methods (`in`, `startswith`, `replace`)
2. Compiled regex patterns
3. Non-compiled regex (re.search, etc.)
4. Complex regex with backtracking
5. Nested/recursive regex

**Resource Hierarchy (simplest to most powerful):**

1. String methods
2. Standard `re` module
3. `regex` module (more features)
4. Specialized libraries (email-validator, BeautifulSoup, etc.)
5. Parser libraries (pyparsing, lark, PLY)

For more information:

- [General regex syntax](./regex.md)
- [Python re module reference](./regex_python.md)
- [Official Python documentation](https://docs.python.org/3/library/re.html)
- [Regular-Expressions.info](https://www.regular-expressions.info/)
