#!/usr/bin/python -tt
"""Solve Google Code Jam Qualification Round Africa 2010 Problem A
(https://code.google.com/codejam/contest/351101/dashboard#s=p0) --
Store Credit
"""

import sys


def read_input():
    """Parses input data from stdin.

    Args:
        None

    Returns:
        List of test cases, each of which is tuple (credit, items), where
        'credit' is integer store credit amount and 'items' is list of
        integers representing prices of available items
    """

    lines = sys.stdin.read().splitlines()
    num_test_cases = int(lines[0])

    # each test case consists of 3 lines of data; not counting first line,
    # number of lines must be multiple of 3
    assert (len(lines) - 1) % 3 == 0

    i = 1
    test_cases = []
    while i < len(lines):
        credit = int(lines[i + 0])
        num_items = int(lines[i + 1])
        items = [int(x) for x in lines[i + 2].split()]
        assert len(items) == num_items
        test_cases.append((credit, items))
        i += 3
    assert len(test_cases) == num_test_cases
    return test_cases


def solve_test_case(test_case):
    """Solves single problem test case.

    Args:
        Tuple (credit, items), where 'credit' is integer store credit amount
        and 'items' is list of integers representing prices of available items

    Returns:
        Tuple of two zero-based indices in 'items' whose corresponding values
        sum to 'credit'
    """

    # Problem appears to be a kind of knap-sack problem: which items to put in
    # knapsack so as to exactly fill knapsack. Seems we'll have to use brute
    # force to obtain correct answers.
    # Large data set has 50 cases of up to 2000 items. O(n^2) approach should be
    # fine with data set of that size.
    (credit, items) = test_case
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] + items[j] == credit:
                return (i, j)
    # no solution found; must not happen according to problem specs
    assert False


def main():
    test_cases = read_input()
    i = 1
    for test_case in test_cases:
        solution = solve_test_case(test_case)
        assert solution[0] != solution[1]
        assert solution[0] < solution[1]
        print 'Case #%d: %d %d' % (i, solution[0] + 1, solution[1] + 1)
        i += 1

if __name__ == '__main__':
    main()
