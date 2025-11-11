## Exercise 702: Capitalizing I

Use substitution to replace every occurrence of the word `i` with the word `I` (uppercase, I as in me).

A regex match is replaced with the text in the substitution field when using substitution.

### Task:
Write a Python function that uses regex substitution to replace every standalone lowercase `i` (the pronoun) with uppercase `I`.

### Examples:
```python
# Should transform correctly
capitalize_i("i'm replacing it. am i not?")
# Returns: "I'm replacing it. am I not?"

capitalize_i("i think i can do this")
# Returns: "I think I can do this"

capitalize_i("if i understand correctly")
# Returns: "if I understand correctly"
```

<details>
    <summary>Hint</summary>
    Use `re.sub()` for substitution in Python. The word boundary `\b` ensures you only match the standalone letter `i`, not `i` inside words like "if", "it", or "think".
</details>
