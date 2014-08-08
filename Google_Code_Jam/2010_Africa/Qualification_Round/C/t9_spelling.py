#!/usr/bin/python -tt

"""Solves Google Code Jam Qualification Round Africa 2010 Problem C
(https://code.google.com/codejam/contest/351101/dashboard#s=p2)
"T9 Spelling"
"""

import sys


def get_t9_dict():
    """Generates dictionary mapping character to keypress sequence

    Args:
        None

    Returns:
        Dict mapping single-characters string in set '[a-z] ' (i.e. lower-case
        alphabetic and space) to keypress sequence represented as string
        (e.g. 'c': '222')
    """

    # each element contains characters represented by element index's key number
    # in proper order (e.g. if 'b' should map to '22', then 'b' should be second
    # character in string which has index 2)
    keys = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    t9_dict = {}
    for key_number in range(len(keys)):
        letters = keys[key_number]
        for i in range(len(letters)):
            t9_dict[letters[i]] = str(key_number) * (i + 1)
        key_number += 1
    return t9_dict


def read_input():
    """Parses problem data on stdin.

    Args:
        None

    Returns:
        List of test case strings in order provided

    Raises:
        AssertionError: on invalid input (claimed number of test cases does
                        not match actual number)
    """

    lines = sys.stdin.read().splitlines()
    num_test_cases = int(lines[0])
    test_cases = lines[1:]
    assert len(test_cases) == num_test_cases
    return test_cases


def string_to_t9(t9_dict, text):
    """Generates string's keypress sequence.

    Args:
        t9_dict: dictionary mapping characters in set '[a-z] ' to keypress
        sequence string (e.g. 'c': '222')
        text: string whose keypress sequence to be generated

    Returns:
        String representing keypress-sequence representation of argument 'text'
    """

    t9_list = []
    for char in text:
        if not char.isalpha() and char != ' ':
            continue
        char = char.lower()
        t9_string = t9_dict[char]
        # insert space if current key same as previous
        if len(t9_list) > 0 and t9_string[0] == t9_list[-1][0]:
            t9_list.append(' ')
        t9_list.append(t9_string)
    return ''.join(t9_list)


def main():
    test_cases = read_input()
    t9_dict = get_t9_dict()
    i = 1
    for test_case in test_cases:
        test_case_t9 = string_to_t9(t9_dict, test_case)
        print 'Case #%d: %s' % (i, test_case_t9)
        i += 1


if __name__ == '__main__':
    main()
