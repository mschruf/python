#!/usr/bin/python -tt

"""Solves Google Code Jam 2014 Round 3 Problem A
(https://code.google.com/codejam/contest/3024486/dashboard#s=p0)
"Magical, Marvelous Tour"

NOTE: algorithm does not scale to Large dataset
"""

import sys


def read_input():
    """Parses problem data from stdin.

    Args:
        None

    Returns:
        List of test cases, in order specified, each of which is list of
        integers representing values of n, p, q, r, s, in that order
    """

    lines = sys.stdin.read().splitlines()
    num_test_cases = int(lines[0])
    assert num_test_cases == len(lines) - 1
    test_cases = []
    for line in lines[1:]:
        test_cases.append([int(x) for x in line.split()])
    return test_cases


def get_best_range(devices):
    """Determines best choice of range for Arnar.

    Args:
        devices: list of integers where value of element i is number of
        transistors in device i

    Returns:
        Tuple consisting of tuple of indices defining range and integer of
        number of transistors in range Arnar will choose
    """

    # Since Solveig will always choose interval with most transistors, Arnar's
    # best chance of winning is with whatever partition which maximizes the
    # number of transistors in the interval with the second-highest number of
    # transistors.

    # brute-force approach: try all possible partitions; however, we don't
    # recompute the number of devices in each of the three intervals from
    # scratch; rather, we set them at the start and update them with at most a
    # one addition or subtraction as we change the partitions

    num_best = 0
    range_best = (0, 0)

    # generate array with cumulative transistor sum for each device index, i.e.
    # element i reflects number of transistors in devices with indices < i
    cumulative_sums = [0]
    for i in range(1, len(devices) + 1):
        cumulative_sums.append(cumulative_sums[i - 1] + devices[i - 1])

    for i in range(len(devices)):
        for j in range(i, len(devices)):
            interval_sums = [cumulative_sums[i],
                             cumulative_sums[j + 1] - cumulative_sums[i],
                             cumulative_sums[len(devices)] -
                             cumulative_sums[j + 1]]
            assert sum(interval_sums) == cumulative_sums[len(devices)]
            # NOTE: following is faster than sorting list of 3 elements and
            # adding elements 0 and 1
            num_arnar = cumulative_sums[len(devices)] - max(interval_sums)
            if num_arnar > num_best:
                num_best = num_arnar
                range_best = (i, j)
    return (range_best, num_best)


def main():
    test_cases = read_input()
    i = 1
    for test_case in test_cases:
        (n, p, q, r, s) = test_case
        devices = [(x * p + q) % r + s for x in range(n)]
        num_transistors_total = sum(devices)
        ((range_start, range_end), num_transistors_arnar) = \
            get_best_range(devices)
        probability_win = num_transistors_arnar / float(num_transistors_total)
        print 'Case #%d: %.10f' % (i, probability_win)
        i += 1


if __name__ == '__main__':
    main()
