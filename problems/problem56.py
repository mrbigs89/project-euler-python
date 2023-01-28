# A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one
# followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
from utils import sum_digits


def solve():
    max_sum = 0
    for a in range(1, 101):
        for b in range(1, 101):
            current_sum = sum_digits(a ** b)
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum


if __name__ == '__main__':
    print(solve())
