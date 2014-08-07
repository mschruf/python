#!/usr/bin/python -tt

"""Solves Google Code Jam 2010 Round 1C Problem A
(https://code.google.com/codejam/contest/619102/dashboard#s=p0)
"Rope Intranet"
"""

import sys


def read_input():
    """Parses problem data from stdin.

    Args:
        None

    Returns:
        List of test cases, each of which is list of tuples of wire data
        (height_on_side_a, height_on_side_b)
    """

    lines = sys.stdin.read().splitlines()
    num_test_cases = int(lines[0])
    test_cases = []
    i = 1
    for _ in range(num_test_cases):
        wires = []
        num_wires = int(lines[i])
        i += 1
        for _ in range(num_wires):
            # map() ungood :(
            #(height_a, height_b) = map(int, lines[i].split())
            (height_a, height_b) = [int(x) for x in lines[i].split()]
            wires.append((height_a, height_b))
            i += 1
        test_cases.append(wires)
    return test_cases


def solve(wires):
    """Calculates number of intersections given list of wires.

    Args:
        List of tuples of wire data (height_on_side_a, height_on_side_b)

    Returns:
        Integer representing total number of wire intersections given specified
        wire data
    """

    # Approach: if there's an algorithm faster than O(n^2), it doesn't occur to
    # me at the moment; so, we'll check all n-choose-2 wire combinations:
    # repeatedly remove a wire from the list and test it for intersection with
    # all wires remaining in the list
    num_intersections = 0
    while wires:
        wire = wires.pop()
        for wire_other in wires:
            # wires cross if their points don't have the same relationship on
            # both sides, with respect to which is higher; i.e. if wire A's
            # attachment points are both higher or both lower than wire B's,
            # A and B don't cross
            if ((wire[0] < wire_other[0] and wire[1] > wire_other[1]) or
                (wire[0] > wire_other[0] and wire[1] < wire_other[1])):
                num_intersections += 1
    return num_intersections


def main():
    test_cases = read_input()
    i = 1
    for test_case in test_cases:
        num_intersections = solve(test_case)
        print 'Case #%d: %d' % (i, num_intersections)
        i += 1


if __name__ == '__main__':
    main()
