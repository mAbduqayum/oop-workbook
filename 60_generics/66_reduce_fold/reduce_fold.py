from typing import Callable


def reduce[T, U](items: list[T], func: Callable[[U, T], U], initial: U) -> U:
    result = initial
    for item in items:
        result = func(result, item)
    return result
