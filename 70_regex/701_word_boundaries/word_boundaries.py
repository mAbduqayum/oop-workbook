import re


def contains_word(text: str) -> bool:
    pattern = r'\bword\b'
    return bool(re.search(pattern, text, re.IGNORECASE))


if __name__ == "__main__":
    # Test cases that should return True
    print(f"{contains_word('I heard that word before') = }")
    print(f"{contains_word('Word is the word') = }")
    print(f"{contains_word('WORD') = }")
    
    # Test cases that should return False
    print(f"{contains_word('password') = }")
    print(f"{contains_word('wording') = }")
    print(f"{contains_word('sword') = }")
