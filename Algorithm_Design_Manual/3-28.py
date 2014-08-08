#!/usr/bin/python -tt

"""O(n) time and O(n) space solution to problem 3-28 from
/The Algorithm Design Manual/, 2nd ed., by Steven Skiena
"""

import operator, random


def calculate_m(x):
    """Calculates values of array M without using division.

    Args:
        x: list of n integers

    Returns:
        List of n elements where i-th element is product of all integers in
        argument 'x' except for x[i]
    """

    intermediate_products_1 = [1]
    for i in range(len(x) - 1):
        intermediate_products_1.append(x[i] * intermediate_products_1[i])
    intermediate_products_2 = [1] * len(x)
    for i in range(len(x) - 2, -1, -1):
        intermediate_products_2[i] = x[i + 1] * intermediate_products_2[i + 1]
    m = [intermediate_products_1[i] * intermediate_products_2[i]
         for i in range(len(x))]
    return m


def main():
    LEN_X = 5
    x = [random.randrange(1, 101) for _ in range(LEN_X)]
    print 'X = ', x
    m = calculate_m(x)
    print 'M = ', m
    product_complete = reduce(operator.mul, x)
    for i in range(len(m)):
        assert m[i] == product_complete / x[i]


if __name__ == '__main__':
    main()
