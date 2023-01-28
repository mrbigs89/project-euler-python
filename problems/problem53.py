# <p>There are exactly ten ways of selecting three from five, 12345:</p> <p class="center">123, 124, 125, 134, 135,
# 145, 234, 235, 245, and 345</p> <p>In combinatorics, we use the notation, $\displaystyle \binom 5 3 = 10$.</p>
# <p>In general, $\displaystyle \binom n r = \dfrac{n!}{r!(n-r)!}$, where $r \le n$, $n! = n \times (n-1) \times ...
# \times 3 \times 2 \times 1$, and $0! = 1$. </p> <p>It is not until $n = 23$, that a value exceeds one-million:
# $\displaystyle \binom {23} {10} = 1144066$.</p> <p>How many, not necessarily distinct, values of $\displaystyle
# \binom n r$ for $1 \le n \le 100$, are greater than one-million?</p>

from math import comb


def solve() -> int:
    count = 0
    for n in range(1, 101):
        if n % 10 == 0:
            print(n)
        for k in range(0, n + 1):
            res = comb(n, k)
            if res > 1000000:
                print(f"{n}, {k}: {res}")
                count += 1
    return count


if __name__ == '__main__':
    print(solve())
