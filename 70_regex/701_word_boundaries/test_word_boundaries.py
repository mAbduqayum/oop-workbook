import pytest
from word_boundaries import contains_word


class TestContainsWord:
    @pytest.mark.parametrize(
        "text, expected, error_msg",
        [
            # True cases - standalone word "word"
            (
                "I heard that word before",
                True,
                "Should find 'word' as standalone word in sentence"
            ),
            (
                "Word is the word",
                True,
                "Should match 'word' case-insensitively (Word/word)"
            ),
            (
                "WORD",
                True,
                "Should match uppercase 'WORD' (case-insensitive)"
            ),
            (
                "A word.",
                True,
                "Should find 'word' followed by punctuation (word boundary)"
            ),
            (
                "(word)",
                True,
                "Should find 'word' surrounded by punctuation (word boundaries)"
            ),
            
            # False cases - "word" as part of another word
            (
                "password",
                False,
                "Should NOT match 'word' inside 'password' (not a word boundary)"
            ),
            (
                "wording",
                False,
                "Should NOT match 'word' at start of 'wording' (not a word boundary)"
            ),
            (
                "sword",
                False,
                "Should NOT match 'word' at end of 'sword' (not a word boundary)"
            ),
            (
                "",
                False,
                "Empty string should return False"
            ),
            (
                "wo rd",
                False,
                "Should NOT match 'wo rd' with space in middle (not the word 'word')"
            ),
        ],
    )
    def test_contains_word(self, text, expected, error_msg):
        result = contains_word(text)
        assert result == expected, (
            f"{error_msg}\n"
            f"Input: '{text}'\n"
            f"Expected: {expected}\n"
            f"Got: {result}"
        )
