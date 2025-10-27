from typing import Callable


def filter_items[T](items: list[T], predicate: Callable[[T], bool]) -> list[T]:
    return [item for item in items if predicate(item)]
