# Leonhard Euler was born on 15 April 1707.
# Consider the sequence 1504170715041707n mod 4503599627370517.
# An element of this sequence is defined to be an Eulercoin if it is strictly smaller than all previously found
# Eulercoins.
# For example, the first term is 1504170715041707 which is the first Eulercoin. The second term is 3008341430083414
# which is greater than 1504170715041707 so is not an Eulercoin. However, the third term is 8912517754604 which is
# small enough to be a new Eulercoin.
# The sum of the first 2 Eulercoins is therefore 1513083232796311.
# Find the sum of all Eulercoins.
import math


def solve():
    start = 1504170715041707
    base = 4503599627370517
    midpoint = 15806432
    bottom_up_eulercoins = [start]
    candidate = start
    total = 0
    for n in range(1, base):
        candidate = (candidate + start) % base
        if candidate < bottom_up_eulercoins[-1]:
            print(candidate)
            bottom_up_eulercoins.append(candidate)
            total += candidate
        if candidate == midpoint:
            break
    inverse = pow(start, -1, base)
    last_n = inverse
    top_down_eulercoins = [1]
    for candidate in range(2, midpoint):
        candidate_n = (inverse * candidate) % base
        if candidate_n < last_n:
            last_n = candidate_n
            top_down_eulercoins += [candidate]
            total += candidate
            print(candidate)
    return sum(bottom_up_eulercoins + top_down_eulercoins)


if __name__ == '__main__':
    print(solve())
