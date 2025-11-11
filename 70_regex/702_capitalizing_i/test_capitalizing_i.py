import pytest
from capitalizing_i import capitalize_i


class TestCapitalizeI:
    @pytest.mark.parametrize(
        "text, expected, error_msg",
        [
            (
                "i'm replacing it. am i not?",
                "I'm replacing it. am I not?",
                "Should capitalize standalone 'i' but not 'i' inside 'it'"
            ),
            (
                "i think i can do this",
                "I think I can do this",
                "Should capitalize multiple standalone 'i' occurrences"
            ),
            (
                "if i understand correctly",
                "if I understand correctly",
                "Should capitalize 'i' but not 'i' inside 'if'"
            ),
            (
                "i i i",
                "I I I",
                "Should capitalize all standalone 'i' characters"
            ),
            (
                "i",
                "I",
                "Should capitalize single standalone 'i'"
            ),
            (
                "it is impossible",
                "it is impossible",
                "Should NOT capitalize 'i' inside words like 'it', 'is', 'impossible'"
            ),
            (
                "i'd like to go",
                "I'd like to go",
                "Should capitalize 'i' in contractions like \"i'd\""
            ),
            (
                "will i?",
                "will I?",
                "Should capitalize 'i' before punctuation"
            ),
            (
                "(i)",
                "(I)",
                "Should capitalize 'i' surrounded by punctuation"
            ),
            (
                "CAPITAL I",
                "CAPITAL I",
                "Should NOT change uppercase 'I' or other text"
            ),
        ],
    )
    def test_capitalize_i(self, text, expected, error_msg):
        result = capitalize_i(text)
        assert result == expected, (
            f"{error_msg}\n"
            f"Input:    '{text}'\n"
            f"Expected: '{expected}'\n"
            f"Got:      '{result}'"
        )
