from dataclasses import dataclass

import pytest
from the_queue import Queue


def test_enqueue_adds_items():
    queue = Queue[int]()
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.size() == 2


def test_dequeue_returns_items_in_fifo_order():
    queue = Queue[int]()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30


def test_peek_returns_front_without_removing():
    queue = Queue[int]()
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.peek() == 10
    assert queue.size() == 2


def test_is_empty_returns_true_for_empty_queue():
    queue = Queue[int]()
    assert queue.is_empty() is True


def test_is_empty_returns_false_for_non_empty_queue():
    queue = Queue[int]()
    queue.enqueue(10)
    assert queue.is_empty() is False


def test_size_returns_correct_count():
    queue = Queue[int]()
    assert queue.size() == 0
    queue.enqueue(10)
    assert queue.size() == 1
    queue.enqueue(20)
    assert queue.size() == 2
    queue.dequeue()
    assert queue.size() == 1


def test_dequeue_from_empty_queue_raises_error():
    queue = Queue[int]()
    with pytest.raises(IndexError):
        queue.dequeue()


def test_peek_from_empty_queue_raises_error():
    queue = Queue[int]()
    with pytest.raises(IndexError):
        queue.peek()


def test_queue_with_strings():
    queue = Queue[str]()
    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")
    assert queue.dequeue() == "first"
    assert queue.dequeue() == "second"


def test_queue_with_custom_class():
    @dataclass
    class PrintJob:
        document: str
        pages: int

    queue = Queue[PrintJob]()
    job1 = PrintJob("report.pdf", 10)
    job2 = PrintJob("invoice.pdf", 2)
    queue.enqueue(job1)
    queue.enqueue(job2)
    assert queue.dequeue() == job1
    assert queue.dequeue() == job2


def test_multiple_operations_maintain_fifo_order():
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    queue.enqueue(4)
    queue.enqueue(5)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4


def test_fifo_ordering_strictly_maintained():
    queue = Queue[str]()
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    assert queue.dequeue() == "A"
    assert queue.peek() == "B"
    assert queue.dequeue() == "B"
