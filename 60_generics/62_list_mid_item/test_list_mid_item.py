import pytest
from list_mid_item import get_mid_item


def test_get_mid_item_odd_length_int():
    assert get_mid_item([1, 2, 3, 4, 5]) == 3


def test_get_mid_item_even_length_int():
    assert get_mid_item([1, 2, 3, 4]) == 2


def test_get_mid_item_single_element():
    assert get_mid_item([42]) == 42


def test_get_mid_item_two_elements():
    assert get_mid_item([10, 20]) == 10


def test_get_mid_item_str_list():
    assert get_mid_item(["a", "b", "c"]) == "b"


def test_get_mid_item_float_list():
    assert get_mid_item([1.1, 2.2, 3.3, 4.4, 5.5]) == 3.3


def test_get_mid_item_empty_list():
    with pytest.raises(ValueError, match="List is empty"):
        get_mid_item([])


def test_get_mid_item_uses_generics():
    assert hasattr(get_mid_item, "__type_params__")
    assert len(get_mid_item.__type_params__) == 1
    assert get_mid_item.__type_params__[0].__name__ == "T"
