#!/usr/bin/python -tt

"""Solves Google Code Jam 2008 Round 1A problem A
(https://code.google.com/codejam/contest/32016/dashboard#s=p0)
"Minimum Scalar Product"
"""

import sys

def read_input():
    """Reads problem data from stdin.
    Args:
        None

    Returns:
        List of test cases, each of which is list of two vectors, which are
        themselves lists

    Raises:
        AssertionError: on invalid input data
    """

    lines = sys.stdin.read().splitlines()
    num_test_cases = int(lines[0])
    test_case_lines = lines[1:]
    assert num_test_cases * 3 == len(test_case_lines)
    test_cases = []
    for i in range(0, num_test_cases * 3, 3):
        num_vector_elements = int(test_case_lines[i + 0])
        # pylint says use of map() discouraged; :( seems more elegant
        #vectors = [ map(int, test_case_lines[i + 1].split()),
        #            map(int, test_case_lines[i + 2].split())]
        vectors = [[int(x) for x in test_case_lines[i + 1].split()],
                   [int(x) for x in test_case_lines[i + 2].split()]]
        assert len(vectors[0]) == len(vectors[1]) == num_vector_elements
        test_cases.append(vectors)
    assert len(test_cases) == num_test_cases
    return test_cases


def main():
    """Computes minimum scalar product for each test case.
    """
    test_cases = read_input()
    i = 1
    for test_case in test_cases:
        vectors = test_case
        # minimum scalar product obtained when we multiply greatest factors by
        # least factors, so we'll sort the two vectors in opposite order to
        # facilitate this

        # pylint says use of map() discouraged; :( seems more elegant
        #min_scalar_product = sum(map(operator.mul, sorted(vector[0]),
        #                             sorted(vector[1], reverse=True)))
        min_scalar_product = sum([x * y for x, y in
                                  zip(sorted(vectors[0]),
                                      sorted(vectors[1], reverse=True))])
        print 'Case #%d: %d' % (i, min_scalar_product)
        i += 1


if __name__ == '__main__':
    main()
