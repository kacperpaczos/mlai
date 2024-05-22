from typing import Callable, Any
from timeit import timeit
from functools import wraps


def memoize(fun: Callable):
    @wraps(fun)
    def wrapper(*args: Any, **kwargs: Any):
        key = (args, frozenset(kwargs.items()))
        if key not in wrapper.cache:
            wrapper.cache[key] = fun(*args, **kwargs)
        return wrapper.cache[key]

    wrapper.cache = {}
    return wrapper


if __name__ == "__main__":
    def naive_fibonacci(n: int) -> int:
        if n < 2:
            return n
        else:
            return naive_fibonacci(n - 2) + naive_fibonacci(n - 1)


    @memoize  # można tak udekorować każdą czystą funkcję
    def memoized_fibonacci(n: int) -> int:  # oprócz dekoratora i nazwy ten sam kod
        if n < 2:
            return n
        else:
            return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


    # sprawdzenie poprawności - wartości się zgadzają
    for i in range(25):
        print(naive_fibonacci(i), memoized_fibonacci(i))

    # porównanie czasu wykonania:
    print(timeit("naive_fibonacci(10)", globals=globals()))
    print(timeit("memoized_fibonacci(10)", globals=globals()))
