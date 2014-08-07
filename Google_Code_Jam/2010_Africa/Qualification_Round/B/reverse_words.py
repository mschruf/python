#!/usr/bin/python -tt

"""Solves problem B from Google Code Jam Qualification Round Africa 2010
(https://code.google.com/codejam/contest/351101/dashboard#s=p1)
"Reverse Words"
"""

import sys

def main():
    """Reads problem data from stdin and prints answers to stdout.

    Args:
        None

    Returns:
        Nothing
    """

    lines = sys.stdin.read().splitlines()
    num_test_cases = int(lines[0])
    test_cases = lines[1:]
    assert len(test_cases) == num_test_cases
    i = 1
    for test_case in test_cases:
        words = test_case.split()
        words.reverse()
        print 'Case #%d:' % (i,), ' '.join(words)
        i += 1


if __name__ == '__main__':
    main()
