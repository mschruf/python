#!/usr/bin/python -tt

"""Solves Google Code Jam 2009 Qualification Round Problem A
(https://code.google.com/codejam/contest/90101/dashboard#s=p0)
"Alien Language"
"""

import sys


def read_input():
    """Reads problem data from stdin and returns structured data.

    Args:
        None

    Returns:
        Tuple composed of (a) list of strings comprising known words and (b)
        list of strings comprising test cases

    Raises:
        AssertionError: on invalid input
    """

    lines = sys.stdin.read().splitlines()
    (_, num_words, num_test_cases) = [int(x) for x in lines[0].split()]
    words = lines[1:num_words + 1]
    test_cases = lines[num_words + 1:]
    assert len(test_cases) == num_test_cases
    return (words, test_cases)


def get_candidate_characters(test_case):
    """Converts test case string into list where element i is string of
    candidate characters for position i."""

    state_in_multiple = False
    pattern_chars = []
    for i in range(len(test_case)):
        char = test_case[i]
        if char == '(':
            chars = []
            state_in_multiple = True
        elif char == ')':
            pattern_chars.append(''.join(chars))
            state_in_multiple = False
        elif char.isalpha():
            if state_in_multiple:
                chars.append(char)
            else:
                pattern_chars.append(char)
        else:
            assert False # invalid data
    return pattern_chars


def get_num_word_matches(words, test_case):
    """Returns number of known words which match test case."""

    pattern_chars = get_candidate_characters(test_case)
    assert len(pattern_chars) == len(words[0])

    candidates = words[:]
    for i in range(len(words[0])):
        candidates_new = []
        for word in candidates:
            if word[i] in pattern_chars[i]:
                candidates_new.append(word)
        candidates = candidates_new[:]
        if not candidates:
            break
    return len(candidates)


def main():
    (words, test_cases) = read_input()
    i = 1
    for test_case in test_cases:
        num_matches = get_num_word_matches(words, test_case)
        print 'Case #%d: %d' % (i, num_matches)
        i += 1


if __name__ == '__main__':
    main()
