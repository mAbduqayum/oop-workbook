from typing import Iterator


class Node[T]:
    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Node[T] | None = None


class LinkedList[T]:
    def __init__(self) -> None:
        self._head: Node[T] | None = None
        self._size = 0

    def append(self, value: T) -> None:
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, value: T) -> None:
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def find(self, value: T) -> T | None:
        current = self._head
        while current is not None:
            if current.value == value:
                return current.value
            current = current.next
        return None

    def remove(self, value: T) -> bool:
        if self._head is None:
            return False
        if self._head.value == value:
            self._head = self._head.next
            self._size -= 1
            return True
        current = self._head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def is_empty(self) -> bool:
        return self._head is None

    def size(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        values = " -> ".join(repr(v) for v in self)
        return f"LinkedList({values})" if values else "LinkedList()"
