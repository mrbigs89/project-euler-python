# A common security method used for online banking is to ask the user for three random characters from a passcode.
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply
# would be: 317.
# The text file, keylog.txt, contains fifty successful login attempts.
# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest
# possible secret passcode of unknown length.
import functools
from functools import cmp_to_key
from pathlib import Path
from typing import List, Set

from utils import BASE_INPUT_PATH

INPUT_PATH = BASE_INPUT_PATH / 'problem079_keylog'


def read_input(input_path: Path = INPUT_PATH) -> List[str]:
    with open(input_path, 'r') as f:
        return [line.strip() for line in f.readlines()]


def find_constraints(attempts: List[str]) -> Set[str]:
    """return a set of strings AB in which A must be before B in the result"""
    relationships = set()
    for attempt in attempts:
        relationships.add((attempt[:2]))
        relationships.add((attempt[1:]))
    return relationships


def compare_digits_using_constraints(d1: str, d2: str, constraints: Set[str]) -> int:
    if d1 + d2 in constraints:
        return -1
    elif d2 + d1 in constraints:
        return 1
    else:
        return 0


def solve(input_path: Path = INPUT_PATH) -> int:
    attempts = read_input(INPUT_PATH)
    constraints = find_constraints(attempts)
    for constraint in constraints:
        assert ''.join(reversed(constraint)) not in constraints, "LOOP!"
    digits = list(set(''.join(attempts)))
    comparison_function = functools.partial(compare_digits_using_constraints, constraints=constraints)
    passcode = sorted(digits, key=cmp_to_key(comparison_function))
    return int(''.join(passcode))


if __name__ == '__main__':
    print(solve())
