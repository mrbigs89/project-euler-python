# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different
# order. Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
from utils import n_digits, get_digit_at_index


def solve() -> int:
    n = 100
    while True:
        base_n_digits = n_digits(n)
        base_digits = {get_digit_at_index(n, i) for i in range(base_n_digits)}
        all_permutations = True
        for multiplier in range(6, 1, -1):
            multiple = n * multiplier
            if n_digits(multiple) != base_n_digits:
                all_permutations = False
                break
            multiple_digits = set()
            for i in range(base_n_digits):
                digit = get_digit_at_index(multiple, i)
                if digit in base_digits:
                    multiple_digits.add(digit)
            if base_digits != multiple_digits:
                all_permutations = False
                break
        if all_permutations:
            print(f"Permutations: {[n * multiplier for multiplier in range(1, 7)]}")
            return n
        n += 1


if __name__ == '__main__':
    print(solve())
