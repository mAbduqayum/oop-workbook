from find_search import find


def test_find_int_found():
    result = find([1, 2, 3, 4, 5], lambda x: x > 3)
    assert result == 4


def test_find_int_not_found():
    result = find([1, 2, 3], lambda x: x > 10)
    assert result is None


def test_find_str_found():
    result = find(["apple", "banana", "cherry"], lambda s: s.startswith("b"))
    assert result == "banana"


def test_find_str_not_found():
    result = find(["apple", "banana", "cherry"], lambda s: s.startswith("z"))
    assert result is None


def test_find_empty_list():
    result = find([], lambda x: True)
    assert result is None


def test_find_first_match():
    result = find([2, 4, 6, 8], lambda x: x % 2 == 0)
    assert result == 2


def test_find_even_number():
    result = find([1, 3, 5, 6, 7], lambda x: x % 2 == 0)
    assert result == 6


def test_find_dict():
    dicts = [{"age": 10}, {"age": 20}, {"age": 30}]
    result = find(dicts, lambda d: d["age"] > 15)
    assert result == {"age": 20}
