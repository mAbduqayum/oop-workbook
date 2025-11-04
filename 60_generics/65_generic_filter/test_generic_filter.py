from generic_filter import filter_items


def test_filter_items_even():
    result = filter_items([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
    assert result == [2, 4, 6]


def test_filter_items_odd():
    result = filter_items([1, 2, 3, 4, 5, 6], lambda x: x % 2 != 0)
    assert result == [1, 3, 5]


def test_filter_items_greater_than():
    result = filter_items([1, 5, 10, 15, 20], lambda x: x > 10)
    assert result == [15, 20]


def test_filter_items_str_length():
    result = filter_items(["a", "ab", "abc", "abcd"], lambda s: len(s) > 2)
    assert result == ["abc", "abcd"]


def test_filter_items_str_startswith():
    result = filter_items(
        ["apple", "banana", "avocado", "cherry"], lambda s: s.startswith("a")
    )
    assert result == ["apple", "avocado"]


def test_filter_items_none_match():
    result = filter_items([1, 2, 3], lambda x: x > 10)
    assert result == []


def test_filter_items_all_match():
    result = filter_items([2, 4, 6, 8], lambda x: x % 2 == 0)
    assert result == [2, 4, 6, 8]


def test_filter_items_empty_list():
    result = filter_items([], lambda x: True)
    assert result == []


def test_filter_items_uses_generics():
    assert hasattr(filter_items, "__type_params__")
    assert len(filter_items.__type_params__) == 1
    assert filter_items.__type_params__[0].__name__ == "T"
