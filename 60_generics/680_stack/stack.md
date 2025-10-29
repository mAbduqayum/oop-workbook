# Generic Stack

## Exercise: Implement a Generic Stack Data Structure

Implement a generic `Stack[T]` class that provides Last-In-First-Out (LIFO) behavior. Your stack should use Python's built-in list internally but expose a clean, type-safe interface.

**Why This Matters:**

Stacks are fundamental data structures used throughout software engineering. From managing function call frames in programming languages to implementing undo/redo functionality in applications, stacks solve the problem of tracking operations in reverse order. By making your stack generic, you enable it to work with any type while maintaining type safety—the Python type checker will catch mistakes like trying to pop a string from a stack of integers. This is your first step from generic functions to generic data structures, teaching you how type parameters work with classes and their methods.

In real-world applications, you'll see stacks managing browser history, expression evaluation in calculators, depth-first search in graphs, and syntax parsing in compilers. A well-designed generic stack provides a reusable component that works seamlessly with any type your application needs.

**Example Usage:**

```python
# Basic usage with integers
numbers = Stack[int]()
numbers.push(10)
numbers.push(20)
numbers.push(30)
print(numbers.peek())  # 30 (most recent)
print(numbers.pop())   # 30
print(numbers.pop())   # 20
print(numbers.size())  # 1

# String stack
words = Stack[str]()
words.push("first")
words.push("second")
words.push("third")
print(words.pop())  # "third" (LIFO!)

# Empty stack handling
empty_stack = Stack[float]()
print(empty_stack.is_empty())  # True
try:
    empty_stack.pop()  # Should raise IndexError
except IndexError as e:
    print(f"Error: {e}")

# Type safety demonstration
typed_stack = Stack[int]()
typed_stack.push(42)
# typed_stack.push("hello")  # Type checker error!
```

**Advanced Example with Custom Types:**

```python
from dataclasses import dataclass

@dataclass
class Task:
    title: str
    priority: int

@dataclass
class Command:
    action: str
    timestamp: float

# Task management (undo stack)
undo_stack = Stack[Command]()
undo_stack.push(Command("delete_file", 1234567890.0))
undo_stack.push(Command("edit_text", 1234567891.0))
undo_stack.push(Command("move_item", 1234567892.0))

# Undo operations in reverse order
while not undo_stack.is_empty():
    cmd = undo_stack.pop()
    print(f"Undoing: {cmd.action} at {cmd.timestamp}")

# Priority task processing
tasks = Stack[Task]()
tasks.push(Task("Low priority task", 1))
tasks.push(Task("Medium priority task", 2))
tasks.push(Task("High priority task", 3))

# Process most recent task first
current = tasks.peek()
print(f"Next task: {current.title} (priority: {current.priority})")
```

**Testing Requirements:**

Your implementation should pass tests that verify:
- Pushing items adds them to the stack
- Popping items removes and returns them in LIFO order
- Peeking returns the top item without removing it
- `is_empty()` returns `True` for empty stacks and `False` otherwise
- `size()` returns the correct number of items
- Popping from an empty stack raises `IndexError`
- Peeking at an empty stack raises `IndexError`
- The stack maintains type safety with different types (int, str, custom classes)
- Multiple push operations followed by multiple pop operations maintain correct order
- The stack works correctly with None as a valid value (if T allows it)
