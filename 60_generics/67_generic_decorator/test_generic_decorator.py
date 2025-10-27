import time
from dataclasses import dataclass

import pytest
from generic_decorator import timer


def test_decorator_returns_value(capsys):
    @timer
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert "Function 'add' took" in captured.out
    assert "seconds" in captured.out


def test_decorator_times_function(capsys):
    @timer
    def slow_function():
        time.sleep(0.01)

    slow_function()

    captured = capsys.readouterr()
    assert "Function 'slow_function' took" in captured.out
    assert float(captured.out.split()[3]) >= 0.01


def test_decorator_preserves_function_name():
    @timer
    def my_function():
        pass

    assert my_function.__name__ == "my_function"


def test_no_parameters_no_return(capsys):
    @timer
    def do_nothing() -> None:
        time.sleep(0.01)

    result = do_nothing()
    assert result is None

    captured = capsys.readouterr()
    assert "Function 'do_nothing' took" in captured.out


def test_multiple_parameters(capsys):
    @timer
    def add(a: int, b: int, c: int = 0) -> int:
        return a + b + c

    result = add(1, 2, c=3)
    assert result == 6

    captured = capsys.readouterr()
    assert "Function 'add' took" in captured.out


def test_keyword_only_arguments(capsys):
    @timer
    def configure(
        *,
        host: str,
        port: int,
        debug: bool = False,
    ) -> dict[str, str | int | bool]:
        return {"host": host, "port": port, "debug": debug}

    config = configure(host="localhost", port=8080)
    assert config == {"host": "localhost", "port": 8080, "debug": False}

    captured = capsys.readouterr()
    assert "Function 'configure' took" in captured.out


def test_different_return_types(capsys):
    @timer
    def get_string() -> str:
        return "hello"

    @timer
    def get_int() -> int:
        return 42

    @timer
    def get_list() -> list[str]:
        return ["a", "b", "c"]

    @timer
    def get_dict() -> dict[str, int]:
        return {"x": 1, "y": 2}

    assert get_string() == "hello"
    assert get_int() == 42
    assert get_list() == ["a", "b", "c"]
    assert get_dict() == {"x": 1, "y": 2}

    captured = capsys.readouterr()
    assert captured.out.count("Function") == 4
    assert captured.out.count("took") == 4
    assert captured.out.count("seconds") == 4


def test_custom_objects(capsys):
    @dataclass
    class User:
        name: str
        age: int

    @timer
    def create_user(name: str, age: int) -> User:
        return User(name, age)

    user = create_user("Alice", 30)
    assert user.name == "Alice"
    assert user.age == 30

    captured = capsys.readouterr()
    assert "Function 'create_user' took" in captured.out


def test_output_format(capsys):
    @timer
    def test_func():
        time.sleep(0.01)

    test_func()

    captured = capsys.readouterr()
    parts = captured.out.strip().split()
    assert parts[0] == "Function"
    assert parts[1] == "'test_func'"
    assert parts[2] == "took"
    assert parts[4] == "seconds"

    time_value = float(parts[3])
    assert time_value >= 0.01


def test_function_with_exception():
    @timer
    def failing_function():
        raise ValueError("test error")

    with pytest.raises(ValueError, match="test error"):
        failing_function()
