import time
from functools import wraps
from typing import Callable


def timer[**P, T](func: Callable[P, T]) -> Callable[P, T]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Function '{func.__name__}' took {elapsed:.4f} seconds")
        return result

    return wrapper
