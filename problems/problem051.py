# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43,
# 53, 73, and 83, are all prime. By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
# number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113,
# 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest
# prime with this property. Find the smallest prime which, by replacing part of the number (not necessarily adjacent
# digits) with the same digit, is part of an eight prime value family.
from typing import List

from sympy import nextprime

from utils import cached_isprime, nonempty_powerset, n_digits, get_digit_at_index


def reset_ith_digit(base: int, position: int) -> int:  # O(1)
    large_part = base // 10 ** (position + 1) * 10 ** (position + 1)
    small_part = base % 10 ** position
    return large_part + small_part


def solve(num_of_primes: int = 8) -> int:
    n = nextprime(10)
    tested = set()
    while True:
        positions = list(range(n_digits(n)))
        remaining_positions = positions
        while remaining_positions:
            reference_position = remaining_positions[0]
            remaining_positions = remaining_positions[1:]
            reference_digit = get_digit_at_index(n, reference_position)
            base = reset_ith_digit(n, reference_position)
            replaced_positions = [reference_position]
            for i in remaining_positions:
                if get_digit_at_index(n, i) == reference_digit:
                    replaced_positions.append(i)
                    remaining_positions.remove(i)
                    base = reset_ith_digit(base, i)
            ones_positions = sum(10 ** position for position in replaced_positions)
            min_replacement = 1 if replaced_positions[-1] == n_digits(n) - 1 else 0
            candidates = (base + ones_positions * i for i in range(min_replacement, 10))
            allowed_non_primes = 10 - min_replacement - num_of_primes
            for candidate in candidates:
                if allowed_non_primes < 0:
                    break
                if not cached_isprime(candidate):
                    allowed_non_primes -= 1
                else:
                    tested.add(candidate)
            if allowed_non_primes >= 0:
                print(f"Primes: {[base + ones_positions * i for i in range(min_replacement, 10) if cached_isprime(base + ones_positions * i)]}")
                return n
        n = nextprime(n)


if __name__ == '__main__':
    print(solve(8))
