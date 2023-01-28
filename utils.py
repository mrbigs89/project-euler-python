import math
from functools import lru_cache
from itertools import chain, combinations

from sympy import isprime


@lru_cache(maxsize=1000000)
def slow_is_prime(n: int) -> bool:
    return n > 1 and all(n % i > 0 for i in range(2, int(n ** 0.5) + 1))


@lru_cache(maxsize=1000000)
def cached_isprime(n: int) -> bool:
    return isprime(n)


@lru_cache(maxsize=100000)
def nonempty_powerset(iterable):
    """nonempty_powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1)))


@lru_cache(maxsize=1000000)
def n_digits(n: int) -> int:
    return int(math.log10(n)) + 1


def get_digit(number: int, n: int) -> int:
    return number // 10 ** n % 10
