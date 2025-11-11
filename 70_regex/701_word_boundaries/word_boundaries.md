## Exercise 701: Word Boundaries

Check if a string contains the word `word` in it (case-insensitive). 

If you have no idea, I guess you could try `/word/`.

### Task:
Write a Python function that uses regex to check if a string contains the word `word` as a complete word (not as part of another word like "password" or "wording").

### Examples:
```python
# Should return True
contains_word("I heard that word before")
contains_word("Word is the word")
contains_word("WORD")

# Should return False
contains_word("password")
contains_word("wording")
contains_word("sword")
```

<details>
    <summary>Hint:</summary>
    Word boundaries `\b` match positions where a word character is followed by a non-word character, or vice versa.
</details>
