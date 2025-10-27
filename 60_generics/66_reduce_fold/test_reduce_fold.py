from dataclasses import dataclass

import pytest
from reduce_fold import reduce


def test_sum_numbers():
    numbers = [1, 2, 3, 4, 5]
    total = reduce(numbers, lambda acc, x: acc + x, 0)
    assert total == 15


def test_product_numbers():
    numbers = [1, 2, 3, 4, 5]
    product = reduce(numbers, lambda acc, x: acc * x, 1)
    assert product == 120


def test_concatenate_strings():
    words = ["Hello", " ", "World", "!"]
    sentence = reduce(words, lambda acc, word: acc + word, "")
    assert sentence == "Hello World!"


def test_count_elements():
    count = reduce([1, 2, 3, 4, 5], lambda acc, _: acc + 1, 0)
    assert count == 5


def test_find_maximum():
    numbers = [3, 7, 2, 9, 1, 5]
    maximum = reduce(numbers, lambda acc, x: max(acc, x), float("-inf"))
    assert maximum == 9


def test_build_reversed_list():
    numbers = [1, 2, 3, 4]
    reversed_list = reduce(numbers, lambda acc, x: [x] + acc, [])
    assert reversed_list == [4, 3, 2, 1]


def test_empty_list_returns_initial():
    result = reduce([], lambda acc, x: acc + x, 100)
    assert result == 100


def test_count_word_lengths():
    words = ["cat", "elephant", "dog"]
    total_length = reduce(words, lambda acc, word: acc + len(word), 0)
    assert total_length == 14


def test_different_input_output_types():
    strings = ["1", "2", "3"]
    result = reduce(strings, lambda acc, s: acc + int(s), 0)
    assert result == 6


def test_build_dictionary():
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    dict_result = reduce(pairs, lambda acc, pair: {**acc, pair[0]: pair[1]}, {})
    assert dict_result == {"a": 1, "b": 2, "c": 3}


def test_flatten_nested_lists():
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = reduce(nested, lambda acc, lst: acc + lst, [])
    assert flat == [1, 2, 3, 4, 5, 6]


def test_count_occurrences():
    items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    counts = reduce(items, lambda acc, item: {**acc, item: acc.get(item, 0) + 1}, {})
    assert counts == {"apple": 3, "banana": 2, "cherry": 1}


def test_processes_in_correct_order():
    result = reduce([1, 2, 3], lambda acc, x: acc + [x * 2], [])
    assert result == [2, 4, 6]


def test_custom_objects():
    @dataclass
    class Order:
        item: str
        price: float
        quantity: int

    orders = [
        Order("Laptop", 999.99, 2),
        Order("Mouse", 25.50, 5),
        Order("Keyboard", 75.00, 3),
    ]

    total_revenue = reduce(
        orders, lambda acc, order: acc + (order.price * order.quantity), 0.0
    )
    assert abs(total_revenue - 2352.48) < 0.01

    def group_by_price(
        acc: dict[str, list[Order]], order: Order
    ) -> dict[str, list[Order]]:
        category = "expensive" if order.price > 100 else "affordable"
        if category not in acc:
            acc[category] = []
        acc[category].append(order)
        return acc

    grouped = reduce(orders, group_by_price, {})
    assert len(grouped["expensive"]) == 1
    assert len(grouped["affordable"]) == 2

    summary = reduce(
        orders, lambda acc, order: acc + f"{order.quantity}x {order.item}, ", "Order: "
    )
    assert summary == "Order: 2x Laptop, 5x Mouse, 3x Keyboard, "
