from identity_function import identity


def test_identity_int():
    assert identity(42) == 42


def test_identity_str():
    assert identity("hello") == "hello"


def test_identity_float():
    assert identity(3.14) == 3.14


def test_identity_list():
    lst = [1, 2, 3]
    assert identity(lst) == lst


def test_identity_dict():
    d = {"key": "value"}
    assert identity(d) == d


def test_identity_none():
    assert identity(None) is None


def test_identity_bool():
    assert identity(True) is True
    assert identity(False) is False
