from typing import Callable


def find[T](items: list[T], predicate: Callable[[T], bool]) -> T | None:
    for item in items:
        if predicate(item):
            return item
    return None
