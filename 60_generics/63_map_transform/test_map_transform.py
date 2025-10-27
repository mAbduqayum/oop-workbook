from map_transform import map_transform


def test_map_transform_int_to_str():
    result = map_transform([1, 2, 3], lambda x: str(x))
    assert result == ["1", "2", "3"]


def test_map_transform_square():
    result = map_transform([1, 2, 3, 4], lambda x: x * x)
    assert result == [1, 4, 9, 16]


def test_map_transform_str_to_len():
    result = map_transform(["hello", "world", "python"], lambda s: len(s))
    assert result == [5, 5, 6]


def test_map_transform_str_upper():
    result = map_transform(["a", "b", "c"], lambda s: s.upper())
    assert result == ["A", "B", "C"]


def test_map_transform_empty_list():
    result = map_transform([], lambda x: x * 2)
    assert result == []


def test_map_transform_float_to_int():
    result = map_transform([1.5, 2.7, 3.2], lambda x: int(x))
    assert result == [1, 2, 3]


def test_map_transform_tuple_to_sum():
    result = map_transform([(1, 2), (3, 4), (5, 6)], lambda t: t[0] + t[1])
    assert result == [3, 7, 11]
