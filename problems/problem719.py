# <p> We define an $S$-number to be a natural number, $n$, that is a perfect square and its square root can be
# obtained by splitting the decimal representation of $n$ into 2 or more numbers then adding the numbers. </p> <p>
# For example, 81 is an $S$-number because $\sqrt{81} = 8+1$.<br /> 6724 is an $S$-number: $\sqrt{6724} = 6+72+4$.
# <br /> 8281 is an $S$-number: $\sqrt{8281} = 8+2+81 = 82+8+1$.<br /> 9801 is an $S$-number: $\sqrt{9801}=98+0+1$.
# </p> <p> Further we define $T(N)$ to be the sum of all $S$ numbers $n\le N$. You are given $T(10^4) = 41333$. </p>
# <p> Find $T(10^{12})$ </p>
import math
from typing import List

from utils import get_digits


def check_split_result(digits: List[int], split_configuration: int, target: int) -> bool:
    split_choices = "{s:0{width}b}".format(s=split_configuration, width=len(digits) - 1)
    res = 0
    partial_addend = digits[0]
    for i, split_choice in enumerate(split_choices):
        if res + partial_addend > target:
            return False
        if split_choice == '0':
            res += partial_addend
            partial_addend = digits[i + 1]
        else:
            partial_addend = partial_addend * 10 + digits[i + 1]
    res += partial_addend
    return res == target


def is_root_of_s_number(n: int) -> bool:
    square = n * n
    digits = get_digits(square)
    for split_configuration in range(2 ** (len(digits) - 1) - 1, -1, -1):
        if check_split_result(list(reversed(digits)), split_configuration, n):
            print(square)
            return True
    return False


def solve(max_n: int = 10 ** 12):
    max_root = int(math.sqrt(max_n))
    return sum(n * n for n in range(max_root, 3, -1) if (n * n) % 9 in {0, 1} and is_root_of_s_number(n))


if __name__ == '__main__':
    # print(is_root_of_s_number(82))
    print(solve())
