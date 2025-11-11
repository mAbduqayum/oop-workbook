import re


def capitalize_i(text: str) -> str:
    pattern = r'\bi\b'
    return re.sub(pattern, 'I', text)


if __name__ == "__main__":
    # Test cases
    print("Original: i'm replacing it. am i not?")
    print(f"Result:   {capitalize_i("i'm replacing it. am i not?")}\n")
    
    print("Original: i think i can do this")
    print(f"Result:   {capitalize_i('i think i can do this')}\n")
    
    print("Original: if i understand correctly")
    print(f"Result:   {capitalize_i('if i understand correctly')}\n")
    
    print("Original: i i i")
    print(f"Result:   {capitalize_i('i i i')}\n")
