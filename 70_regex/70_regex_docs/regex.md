# Regular Expressions Cheat Sheet

## Basic Syntax

| Pattern | Description                           | Example        | Matches             | Notes                            |
|---------|---------------------------------------|----------------|---------------------|----------------------------------|
| `abc`   | Literal characters                    | `cat`          | "cat" in "category" | Case-sensitive by default        |
| `.`     | Any single character (except newline) | `c.t`          | "cat", "cot", "c9t" | Matches any character            |
| `\.`    | Escaped dot (literal period)          | `file\.txt`    | "file.txt"          | Use `\` to escape metacharacters |
| `\\`    | Escaped backslash                     | `C:\\path`     | "C:\path"           | Backslash needs escaping         |
| `\n`    | Newline character                     | `line1\nline2` | Line break          | Special whitespace character     |
| `\t`    | Tab character                         | `col1\tcol2`   | Tab separator       | Special whitespace character     |
| `\r`    | Carriage return                       | `text\r\n`     | Windows line ending | Often paired with `\n`           |

## Character Classes

| Pattern    | Description                   | Example    | Matches                     | Notes                  |
|------------|-------------------------------|------------|-----------------------------|------------------------|
| `[abc]`    | Any single character from set | `[aeiou]`  | "a", "e", "i", "o", "u"     | Character set          |
| `[^abc]`   | Any character NOT in set      | `[^aeiou]` | Any consonant or non-letter | Negated set            |
| `[a-z]`    | Character range (lowercase)   | `[a-z]`    | Any lowercase letter        | Inclusive range        |
| `[A-Z]`    | Character range (uppercase)   | `[A-Z]`    | Any uppercase letter        | Inclusive range        |
| `[0-9]`    | Digit range                   | `[0-9]`    | Any digit 0-9               | Same as `\d`           |
| `[a-zA-Z]` | Multiple ranges               | `[a-zA-Z]` | Any letter                  | Combine ranges         |
| `[a-z0-9]` | Letters and digits            | `[a-z0-9]` | Alphanumeric (lowercase)    | Multiple ranges        |
| `\d`       | Any digit                     | `\d\d\d`   | "123", "456"                | Shorthand for `[0-9]`  |
| `\D`       | Any non-digit                 | `\D+`      | "abc", "xyz"                | Negated digit          |
| `\w`       | Word character                | `\w+`      | "word", "test123"           | `[a-zA-Z0-9_]`         |
| `\W`       | Non-word character            | `\W+`      | "!", "@#$"                  | Negated word character |
| `\s`       | Whitespace character          | `\s+`      | Space, tab, newline         | ` \t\n\r\f\v`          |
| `\S`       | Non-whitespace character      | `\S+`      | "text", "123"               | Negated whitespace     |

## Quantifiers

| Pattern  | Description            | Example    | Matches                | Notes                               |
|----------|------------------------|------------|------------------------|-------------------------------------|
| `*`      | Zero or more (greedy)  | `ab*c`     | "ac", "abc", "abbc"    | Greedy: matches as much as possible |
| `+`      | One or more (greedy)   | `ab+c`     | "abc", "abbc", "abbbc" | Must match at least once            |
| `?`      | Zero or one (optional) | `colou?r`  | "color", "colour"      | Makes preceding optional            |
| `{n}`    | Exactly n times        | `\d{3}`    | "123", "456"           | Exact count                         |
| `{n,}`   | n or more times        | `\d{3,}`   | "123", "1234", "12345" | Minimum count                       |
| `{n,m}`  | Between n and m times  | `\d{3,5}`  | "123", "1234", "12345" | Range of counts                     |
| `*?`     | Zero or more (lazy)    | `a.*?b`    | "ab" in "axxbxxb"      | Lazy: matches as little as possible |
| `+?`     | One or more (lazy)     | `a.+?b`    | "axb" in "axbxxb"      | Lazy version of `+`                 |
| `??`     | Zero or one (lazy)     | `a.??b`    | "ab" in "axb"          | Lazy version of `?`                 |
| `{n,m}?` | Between n and m (lazy) | `\d{3,5}?` | "123" in "12345"       | Lazy range                          |

## Anchors & Boundaries

| Pattern | Description            | Example   | Matches               | Notes                              |
|---------|------------------------|-----------|-----------------------|------------------------------------|
| `^`     | Start of string/line   | `^Hello`  | "Hello" at start      | With multiline mode: start of line |
| `$`     | End of string/line     | `world$`  | "world" at end        | With multiline mode: end of line   |
| `^...$` | Entire string/line     | `^\d{3}$` | "123" (entire string) | Anchors both ends                  |
| `\b`    | Word boundary          | `\bcat\b` | "cat" in "cat dog"    | Not "category"                     |
| `\B`    | Non-word boundary      | `\Bcat\B` | "cat" in "scat"       | Inside a word                      |
| `\A`    | Start of string only   | `\AHello` | "Hello" at start      | Ignores multiline mode             |
| `\Z`    | End of string only     | `world\Z` | "world" at end        | Ignores multiline mode             |
| `\z`    | Absolute end of string | `world\z` | "world" at very end   | Before any trailing newline        |

## Groups & Capturing

| Pattern         | Description                  | Example                    | Matches        | Notes                    |
|-----------------|------------------------------|----------------------------|----------------|--------------------------|
| `(abc)`         | Capturing group              | `(ab)+`                    | "ab", "abab"   | Captures matched text    |
| `(?:abc)`       | Non-capturing group          | `(?:ab)+`                  | "ab", "abab"   | Groups without capturing |
| `(a\|b)`        | Alternation in group         | `(cat\|dog)`               | "cat" or "dog" | Either/or within group   |
| `(?<name>abc)`  | Named capturing group        | `(?<year>\d{4})`           | "2024"         | Named capture            |
| `(?P<name>abc)` | Named group (Python)         | `(?P<year>\d{4})`          | "2024"         | Python syntax            |
| `\1`            | Backreference to group 1     | `(\w+)\s\1`                | "word word"    | References captured text |
| `\2`            | Backreference to group 2     | `(\w+)-(\w+)-\2`           | "abc-def-def"  | Second capture reference |
| `(?P=name)`     | Named backreference (Python) | `(?P<word>\w+)\s(?P=word)` | "test test"    | Python named reference   |

## Lookaround Assertions

| Pattern               | Description         | Example                    | Matches                      | Notes                        |
|-----------------------|---------------------|----------------------------|------------------------------|------------------------------|
| `(?=...)`             | Positive lookahead  | `\d(?=px)`                 | "5" in "5px"                 | Asserts what follows         |
| `(?!...)`             | Negative lookahead  | `\d(?!px)`                 | "5" in "5em"                 | Asserts what doesn't follow  |
| `(?<=...)`            | Positive lookbehind | `(?<=\$)\d+`               | "10" in "$10"                | Asserts what precedes        |
| `(?<!...)`            | Negative lookbehind | `(?<!\$)\d+`               | "10" in "€10"                | Asserts what doesn't precede |
| `\d(?=px\|em)`        | Multiple conditions | `\d(?=px\|em)`             | "5" in "5px" or "5em"        | Combine with alternation     |
| `(?=.*\d)(?=.*[a-z])` | Multiple lookaheads | `(?=.*\d)(?=.*[a-z]).{8,}` | Password with digit & letter | Chain assertions             |

## Special Constructs

| Pattern         | Description           | Example                   | Matches                         | Notes                     |
|-----------------|-----------------------|---------------------------|---------------------------------|---------------------------|
| `\|`            | Alternation (OR)      | `cat\|dog`                | "cat" or "dog"                  | Either option             |
| `(a\|b\|c)`     | Multiple alternatives | `(jpg\|png\|gif)`         | "jpg", "png", or "gif"          | Group alternatives        |
| `(?i)`          | Case-insensitive flag | `(?i)hello`               | "Hello", "HELLO"                | Inline flag               |
| `(?m)`          | Multiline flag        | `(?m)^line`               | "line" at start of any line     | ^ and $ match line breaks |
| `(?s)`          | Dotall flag           | `(?s).+`                  | Includes newlines               | `.` matches newline       |
| `(?x)`          | Verbose flag          | `(?x) \d+ \s+ \w+`        | Ignores whitespace & comments   | Readable patterns         |
| `(?:...)`       | Non-capturing group   | `(?:https?):`             | Groups without capture overhead | Performance optimization  |
| `(?(1)yes\|no)` | Conditional           | `(\d)?-?(?(1)\d{3}\|\w+)` | Conditional matching            | Advanced pattern          |

## Flags/Modifiers Summary

| Flag | Name             | Description                       | Example Usage                       |
|------|------------------|-----------------------------------|-------------------------------------|
| `i`  | Case-insensitive | Ignore case                       | `/hello/i` matches "Hello", "HELLO" |
| `g`  | Global           | Match all occurrences             | `/\d+/g` finds all numbers          |
| `m`  | Multiline        | `^` and `$` match line boundaries | `/^line/m` matches start of lines   |
| `s`  | Dotall           | `.` matches newlines              | `/begin.*end/s` spans lines         |
| `x`  | Verbose          | Ignore whitespace, allow comments | `/\d{3} \s \d{4}/x` readable format |
| `u`  | Unicode          | Full Unicode support              | `/\p{L}+/u` matches any letters     |
| `y`  | Sticky           | Match from lastIndex              | `/\d+/y` consecutive matches        |

## Common Patterns

### Email Addresses

| Pattern                                          | Description    | Example      | Matches                   | Notes               |
|--------------------------------------------------|----------------|--------------|---------------------------|---------------------|
| `[\w._%+-]+@[\w.-]+\.[A-Za-z]{2,}`               | Basic email    | Full pattern | user@example.com          | Simple validation   |
| `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | Standard email | Full pattern | name.surname@domain.co.uk | More explicit       |
| `^[\w.+-]+@[\w-]+\.[\w.-]+$`                     | Strict email   | Full pattern | test@test.com             | Anchored validation |

### URLs

| Pattern                                                         | Description | Example          | Matches                      | Notes             |
|-----------------------------------------------------------------|-------------|------------------|------------------------------|-------------------|
| `https?://[^\s]+`                                               | Basic URL   | Full pattern     | http://example.com           | Simple match      |
| `https?://[\w.-]+\.[a-z]{2,}`                                   | Domain URL  | Full pattern     | https://example.com          | With domain       |
| `https?://[\w.-]+(?:\.[\w.-]+)+(?:/[\w._~:/?#@!$&'()*+,;=-]*)?` | Full URL    | Complete pattern | https://example.com/path?q=1 | With path & query |

### Phone Numbers

| Pattern                                                      | Description   | Example               | Matches         | Notes            |
|--------------------------------------------------------------|---------------|-----------------------|-----------------|------------------|
| `\d{3}-\d{3}-\d{4}`                                          | US format     | Dashed pattern        | 123-456-7890    | Strict format    |
| `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}`                        | Flexible US   | Flexible pattern      | (123) 456-7890  | Multiple formats |
| `\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}` | International | International pattern | +1-123-456-7890 | Country codes    |

### Dates

| Pattern             | Description           | Example      | Matches    | Notes           |
|---------------------|-----------------------|--------------|------------|-----------------|
| `\d{4}-\d{2}-\d{2}` | ISO date (YYYY-MM-DD) | Date pattern | 2024-12-31 | ISO 8601        |
| `\d{2}/\d{2}/\d{4}` | US date (MM/DD/YYYY)  | Date pattern | 12/31/2024 | US format       |
| `\d{2}-\d{2}-\d{4}` | EU date (DD-MM-YYYY)  | Date pattern | 31-12-2024 | European format |

### Times

| Pattern                      | Description       | Example      | Matches  | Notes          |
|------------------------------|-------------------|--------------|----------|----------------|
| `\d{2}:\d{2}`                | Time (HH:MM)      | Time pattern | 14:30    | 24-hour format |
| `\d{2}:\d{2}:\d{2}`          | Time with seconds | Time pattern | 14:30:45 | Full time      |
| `\d{1,2}:\d{2}\s?(?:AM\|PM)` | 12-hour format    | Time pattern | 2:30 PM  | With AM/PM     |

### IP Addresses

| Pattern                                                                                         | Description | Example    | Matches     | Notes                        |
|-------------------------------------------------------------------------------------------------|-------------|------------|-------------|------------------------------|
| `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`                                                            | Basic IPv4  | IP pattern | 192.168.1.1 | Simple match (not validated) |
| `(?:(?:25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)` | Valid IPv4  | IP pattern | 192.168.1.1 | Validates 0-255 range        |

### File Paths

| Pattern                    | Description  | Example      | Matches             | Notes          |
|----------------------------|--------------|--------------|---------------------|----------------|
| `[\w,\s-]+\.[A-Za-z]{2,4}` | Filename     | File pattern | document.txt        | With extension |
| `/[\w/-]+`                 | Unix path    | Path pattern | /home/user/file.txt | Unix-style     |
| `[A-Za-z]:\\[\w\\-]+`      | Windows path | Path pattern | C:\Users\file.txt   | Windows-style  |

### Username Validation

| Pattern                         | Description                   | Example          | Matches      | Notes        |
|---------------------------------|-------------------------------|------------------|--------------|--------------|
| `^[a-zA-Z0-9_]{3,16}$`          | Alphanumeric username         | Username pattern | user_name123 | 3-16 chars   |
| `^[a-zA-Z][a-zA-Z0-9_-]{2,15}$` | Username (starts with letter) | Username pattern | username123  | Letter first |

### Password Validation

| Pattern                                                                | Description          | Example          | Matches  | Notes                            |
|------------------------------------------------------------------------|----------------------|------------------|----------|----------------------------------|
| `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$`                       | Strong password      | Password pattern | Pass1234 | Upper, lower, digit, 8+ chars    |
| `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$` | Very strong password | Password pattern | Pass@123 | Upper, lower, digit, special, 8+ |

### HTML Tags

| Pattern                                    | Description  | Example         | Matches                 | Notes            |
|--------------------------------------------|--------------|-----------------|-------------------------|------------------|
| `<[^>]+>`                                  | Any HTML tag | Tag pattern     | `<div>`, `<a href="#">` | Basic tag match  |
| `<([a-z]+)([^<]+)*(?:>(.*)<\/\1>\|\s+\/>)` | HTML element | Element pattern | `<div>content</div>`    | With closing tag |
| `<!--.*?-->`                               | HTML comment | Comment pattern | `<!-- comment -->`      | Comments         |

### Credit Card Numbers

| Pattern                                          | Description | Example      | Matches             | Notes             |
|--------------------------------------------------|-------------|--------------|---------------------|-------------------|
| `\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}`         | Card number | Card pattern | 1234-5678-9012-3456 | 16 digits         |
| `^4\d{3}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$`      | Visa        | Card pattern | 4123-4567-8901-2345 | Starts with 4     |
| `^5[1-5]\d{2}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$` | Mastercard  | Card pattern | 5123-4567-8901-2345 | Starts with 51-55 |

### Hexadecimal Colors

| Pattern                    | Description          | Example       | Matches         | Notes        |
|----------------------------|----------------------|---------------|-----------------|--------------|
| `#[0-9A-Fa-f]{6}`          | Hex color (6 digits) | Color pattern | #FF5733         | Full hex     |
| `#[0-9A-Fa-f]{3}`          | Hex color (3 digits) | Color pattern | #F57            | Short hex    |
| `#(?:[0-9A-Fa-f]{3}){1,2}` | Either format        | Color pattern | #FFF or #FFFFFF | Both formats |

### Social Security Numbers (US)

| Pattern             | Description        | Example     | Matches     | Notes           |
|---------------------|--------------------|-------------|-------------|-----------------|
| `\d{3}-\d{2}-\d{4}` | SSN with dashes    | SSN pattern | 123-45-6789 | Standard format |
| `\d{9}`             | SSN without dashes | SSN pattern | 123456789   | No separators   |

### Postal Codes

| Pattern                          | Description          | Example        | Matches             | Notes            |
|----------------------------------|----------------------|----------------|---------------------|------------------|
| `\d{5}(?:-\d{4})?`               | US ZIP code          | ZIP pattern    | 12345 or 12345-6789 | With optional +4 |
| `[A-Z]\d[A-Z]\s?\d[A-Z]\d`       | Canadian postal code | Postal pattern | K1A 0B1             | Canadian format  |
| `[A-Z]{1,2}\d{1,2}\s?\d[A-Z]{2}` | UK postal code       | Postal pattern | SW1A 1AA            | UK format        |

### MAC Addresses

| Pattern                                   | Description | Example     | Matches           | Notes         |
|-------------------------------------------|-------------|-------------|-------------------|---------------|
| `([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})` | MAC address | MAC pattern | 00:1A:2B:3C:4D:5E | Colon or dash |

### Markdown Links

| Pattern                   | Description   | Example      | Matches | Notes                 |
|---------------------------|---------------|--------------|---------|-----------------------|
| `\[([^\]]+)\]\(([^)]+)\)` | Markdown link | Link pattern | `url`   | Captures text and URL |

### Currency

| Pattern                        | Description | Example          | Matches   | Notes           |
|--------------------------------|-------------|------------------|-----------|-----------------|
| `\$\d+(?:,\d{3})*(?:\.\d{2})?` | US Dollar   | Currency pattern | $1,234.56 | With commas     |
| `€\d+(?:\.\d{3})*(?:,\d{2})?`  | Euro        | Currency pattern | €1.234,56 | European format |

## Practical Examples

### Validation Patterns

| Use Case              | Pattern          | Example Input      | Matches                  | Purpose                |
|-----------------------|------------------|--------------------|--------------------------|------------------------|
| Extract digits only   | `\d+`            | "Price: $123.45"   | "123", "45"              | Numbers only           |
| Remove whitespace     | `\s+`            | "hello   world"    | Multiple spaces          | Find whitespace        |
| Find words            | `\b\w+\b`        | "hello-world test" | "hello", "world", "test" | Word extraction        |
| Validate alphanumeric | `^[a-zA-Z0-9]+$` | "Test123"          | Matches                  | Letters & numbers only |
| Extract quoted text   | `"([^"]*)"`      | `"hello world"`    | "hello world"            | Content in quotes      |
| Find duplicated words | `\b(\w+)\s+\1\b` | "the the cat"      | "the the"                | Repeated words         |
| Split by delimiter    | `[;,\|]`         | "a;b,c\|d"         | ";", ",", "\|"           | Multiple delimiters    |
| Trim whitespace       | `^\s+\|\s+$`     | "  text  "         | Leading/trailing spaces  | Trim pattern           |

## Tips & Best Practices

1. **Escape metacharacters**: Use `\` before special characters like `.`, `*`, `+`, `?`, `[`, `]`, `(`, `)`, `{`, `}`,
   `^`, `$`, `|`, `\`
2. **Use non-capturing groups** `(?:...)` when you don't need to extract the matched text (performance)
3. **Be specific**: `\d{3}` is better than `\d+` when you expect exactly 3 digits
4. **Lazy vs Greedy**: Use lazy quantifiers (`*?`, `+?`) when you want minimal matches
5. **Test your patterns**: Regex can be complex; always test with edge cases
6. **Word boundaries**: Use `\b` to match whole words only
7. **Anchors**: Use `^` and `$` to match entire strings, not just parts
8. **Character classes**: `[aeiou]` is clearer than `(a|e|i|o|u)`
9. **Readability**: For complex patterns, use verbose mode `(?x)` and add comments
10. **Performance**: Avoid catastrophic backtracking with nested quantifiers like `(a+)+`
