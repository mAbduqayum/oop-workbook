from typing import Callable


def map_transform[T, U](items: list[T], func: Callable[[T], U]) -> list[U]:
    return [func(item) for item in items]
