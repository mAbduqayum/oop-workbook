# Generic Linked List

## Exercise: Implement a Generic Linked List Data Structure

Implement a generic `LinkedList[T]` class with a nested generic `Node[T]` class. Your linked list should support dynamic insertion and removal while maintaining type safety throughout the node chain.

**Why This Matters:**

Linked lists are fundamental data structures that teach you about memory management, pointers, and dynamic data structures. Unlike arrays or Python lists that allocate contiguous memory, linked lists use nodes that can be scattered throughout memory, connected by references. This makes insertion and deletion at arbitrary positions efficient—no need to shift elements like in arrays.

By implementing a generic linked list with a nested `Node[T]` class, you learn how type parameters work with nested classes and how to maintain type consistency across related components. This pattern appears throughout software engineering: in implementing your own collections, building tree structures, managing undo/redo with more complex operations than simple stacks, or creating memory-efficient data structures for embedded systems.

Real-world applications include music playlists (double-click to skip), implementing LRU caches, managing process scheduling in operating systems, and building the foundation for more complex structures like graphs and trees.

**Example Usage:**

```python
# Basic usage with integers
numbers = LinkedList[int]()
numbers.append(10)
numbers.append(20)
numbers.append(30)
print(numbers.size())  # 3

# Prepend to front
numbers.prepend(5)
# List is now: 5 -> 10 -> 20 -> 30

# Find element
found = numbers.find(20)
print(found)  # 20

not_found = numbers.find(999)
print(not_found)  # None

# Remove element
numbers.remove(20)
# List is now: 5 -> 10 -> 30
print(numbers.size())  # 3

# Visualize the list
print(numbers)  # LinkedList(5 -> 10 -> 30)

# Iterate through the list
for num in numbers:
    print(num)  # 5, then 10, then 30

# Convert to Python list
values = list(numbers)
print(values)  # [5, 10, 30]

# String linked list
words = LinkedList[str]()
words.append("hello")
words.append("world")
words.prepend("say")
# List: "say" -> "hello" -> "world"

# Empty list handling
empty_list = LinkedList[float]()
print(empty_list.is_empty())  # True
print(empty_list.find(3.14))  # None
result = empty_list.remove(3.14)
print(result)  # False (nothing to remove)
```

**Advanced Example with Custom Types:**

```python
from dataclasses import dataclass

@dataclass
class Song:
    title: str
    artist: str
    duration: int

@dataclass
class Task:
    id: int
    description: str
    completed: bool

# Music playlist
playlist = LinkedList[Song]()
playlist.append(Song("Bohemian Rhapsody", "Queen", 354))
playlist.append(Song("Imagine", "John Lennon", 183))
playlist.append(Song("Stairway to Heaven", "Led Zeppelin", 482))

# Add new song to beginning
playlist.prepend(Song("Hey Jude", "The Beatles", 431))

# Find and skip a song
song_to_skip = playlist.find(Song("Imagine", "John Lennon", 183))
if song_to_skip:
    playlist.remove(song_to_skip)
    print(f"Skipped: {song_to_skip.title}")

# Task management
tasks = LinkedList[Task]()
tasks.append(Task(1, "Write code", False))
tasks.append(Task(2, "Write tests", False))
tasks.append(Task(3, "Review PR", False))

# Complete a task
task_to_complete = tasks.find(Task(2, "Write tests", False))
if task_to_complete:
    # In reality, you'd mark it complete and update
    print(f"Found task: {task_to_complete.description}")

# Check list state
print(f"Total tasks: {tasks.size()}")
print(f"List empty: {tasks.is_empty()}")
```

**Testing Requirements:**

Your implementation should pass tests that verify:
- `Node[T]` class correctly stores value and next reference
- Appending items adds them to the end of the list
- Prepending items adds them to the beginning of the list
- `find()` returns the item if found, `None` otherwise
- `remove()` removes the first occurrence of an item and returns `True`, or returns `False` if not found
- `is_empty()` returns `True` for empty lists and `False` otherwise
- `size()` returns the correct number of nodes
- The list maintains type safety with different types (int, str, custom classes)
- Removing from an empty list returns `False` without errors
- Finding in an empty list returns `None` without errors
- Multiple append/prepend operations maintain correct order
- Removing the only element in a list results in an empty list
- The list works with custom dataclass types using equality comparison
- `__repr__()` displays the chain as "LinkedList(item1 -> item2 -> ...)"
- `__repr__()` displays "LinkedList()" for empty lists
- `__iter__()` allows iteration through list items in order
- The list can be converted to a Python list with `list()`
