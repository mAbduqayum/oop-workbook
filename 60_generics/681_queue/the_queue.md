# Generic Queue

## Exercise: Implement a Generic Queue Data Structure

Implement a generic `Queue[T]` class that provides First-In-First-Out (FIFO) behavior. Your queue should use Python's built-in list internally but expose a clean, type-safe interface.

**Why This Matters:**

Queues are essential for managing ordered processing in software systems. Unlike stacks which process items in reverse order, queues maintain fairness by processing items in the order they arrive—just like people waiting in line at a store. From print job spoolers to message queues in distributed systems, from breadth-first search algorithms to task scheduling, queues ensure operations happen in a predictable, first-come-first-served manner.

By implementing a generic queue, you create a reusable component that works with any data type while preserving type safety. Whether you're queuing customer requests, processing events, managing background jobs, or implementing a producer-consumer pattern, a well-designed generic queue provides the foundation. The type system ensures you don't accidentally mix incompatible types in your queue, catching bugs at development time rather than runtime.

**Example Usage:**

```python
# Basic usage with integers
numbers = Queue[int]()
numbers.enqueue(10)
numbers.enqueue(20)
numbers.enqueue(30)
print(numbers.peek())     # 10 (first in)
print(numbers.dequeue())  # 10
print(numbers.dequeue())  # 20
print(numbers.size())     # 1

# String queue
messages = Queue[str]()
messages.enqueue("first")
messages.enqueue("second")
messages.enqueue("third")
print(messages.dequeue())  # "first" (FIFO!)

# Empty queue handling
empty_queue = Queue[float]()
print(empty_queue.is_empty())  # True
try:
    empty_queue.dequeue()  # Should raise IndexError
except IndexError as e:
    print(f"Error: {e}")

# Comparing FIFO vs LIFO behavior
queue = Queue[str]()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print(queue.dequeue())  # "A" - first in, first out

# Stack would give "C" - last in, first out
```

**Advanced Example with Custom Types:**

```python
from dataclasses import dataclass

@dataclass
class PrintJob:
    document: str
    pages: int
    user: str

@dataclass
class Customer:
    name: str
    ticket_number: int
    issue: str

# Print job queue (printer spooler)
print_queue = Queue[PrintJob]()
print_queue.enqueue(PrintJob("report.pdf", 10, "alice"))
print_queue.enqueue(PrintJob("invoice.pdf", 2, "bob"))
print_queue.enqueue(PrintJob("presentation.pdf", 50, "charlie"))

# Process jobs in order
while not print_queue.is_empty():
    job = print_queue.dequeue()
    print(f"Printing {job.document} ({job.pages} pages) for {job.user}")

# Customer service queue
service_queue = Queue[Customer]()
service_queue.enqueue(Customer("Alice", 101, "refund"))
service_queue.enqueue(Customer("Bob", 102, "question"))
service_queue.enqueue(Customer("Charlie", 103, "complaint"))

# Check who's next without removing
next_customer = service_queue.peek()
print(f"Next: {next_customer.name} - Ticket #{next_customer.ticket_number}")

# Serve customers in arrival order
served = service_queue.dequeue()
print(f"Now serving: {served.name} for {served.issue}")
```

**Testing Requirements:**

Your implementation should pass tests that verify:
- Enqueuing items adds them to the queue
- Dequeuing items removes and returns them in FIFO order
- Peeking returns the front item without removing it
- `is_empty()` returns `True` for empty queues and `False` otherwise
- `size()` returns the correct number of items
- Dequeuing from an empty queue raises `IndexError`
- Peeking at an empty queue raises `IndexError`
- The queue maintains type safety with different types (int, str, custom classes)
- Multiple enqueue operations followed by multiple dequeue operations maintain correct order
- The queue works correctly with None as a valid value (if T allows it)
- FIFO ordering is strictly maintained (first item in is first item out)
