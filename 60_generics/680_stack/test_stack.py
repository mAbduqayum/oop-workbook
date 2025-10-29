from dataclasses import dataclass

import pytest
from stack import Stack


def test_push_adds_items():
    stack = Stack[int]()
    stack.push(10)
    stack.push(20)
    assert stack.size() == 2


def test_pop_returns_items_in_lifo_order():
    stack = Stack[int]()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10


def test_peek_returns_top_without_removing():
    stack = Stack[int]()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20
    assert stack.size() == 2


def test_is_empty_returns_true_for_empty_stack():
    stack = Stack[int]()
    assert stack.is_empty() is True


def test_is_empty_returns_false_for_non_empty_stack():
    stack = Stack[int]()
    stack.push(10)
    assert stack.is_empty() is False


def test_size_returns_correct_count():
    stack = Stack[int]()
    assert stack.size() == 0
    stack.push(10)
    assert stack.size() == 1
    stack.push(20)
    assert stack.size() == 2
    stack.pop()
    assert stack.size() == 1


def test_pop_from_empty_stack_raises_error():
    stack = Stack[int]()
    with pytest.raises(IndexError):
        stack.pop()


def test_peek_from_empty_stack_raises_error():
    stack = Stack[int]()
    with pytest.raises(IndexError):
        stack.peek()


def test_stack_with_strings():
    stack = Stack[str]()
    stack.push("first")
    stack.push("second")
    stack.push("third")
    assert stack.pop() == "third"
    assert stack.pop() == "second"


def test_stack_with_custom_class():
    @dataclass
    class Task:
        title: str
        priority: int

    stack = Stack[Task]()
    task1 = Task("Low", 1)
    task2 = Task("High", 3)
    stack.push(task1)
    stack.push(task2)
    assert stack.pop() == task2
    assert stack.pop() == task1


def test_multiple_operations_maintain_order():
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    stack.push(4)
    stack.push(5)
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 2
