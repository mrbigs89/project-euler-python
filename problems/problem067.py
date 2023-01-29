# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
# from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text
# file containing a triangle with one-hundred rows.
#
# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this
# problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over
# twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
from pathlib import Path
from typing import List


INPUT_PATH = Path(__file__).resolve().parent.parent / 'inputs' / 'problem067_triangle.txt'


def read_input(path: Path) -> List[List[int]]:
    res = []
    with open(path, 'r') as f:
        for line in f.readlines():
            res.append([int(c) for c in line.strip().split(' ')])
    return res


def solve():
    triangle = read_input(INPUT_PATH)
    paths = triangle[0]
    for line in triangle[1:]:
        new_paths = []
        for i, number in enumerate(line):
            if i == 0:
                new_paths.append(paths[i] + number)
            elif i == len(paths):
                new_paths.append(paths[i - 1] + number)
            else:
                new_paths.append(number + max(paths[i - 1], paths[i]))
        paths = new_paths
    return max(paths)


if __name__ == '__main__':
    print(solve())
