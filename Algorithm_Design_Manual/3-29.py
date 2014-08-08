#!/usr/bin/python -tt
"""O(n) solution to problem 3-29 from /The Algorithm Design Manual/, 2nd ed.,
by Steven Skiena
"""

import sys


def get_word_pair_counts(filename):
    """Counts word pairs in file.

    Args:
        filename: input file path

    Returns:
        Dictionary mapping word pairs (as strings 'word1 word2') to the number
        of times they appear (as integer) in specified file
    """

    # NOTE: could keep track of items with max count as we go, rather than
    # iterate over dictionary items again later
    with open(filename, 'rU') as file_input:
        words = file_input.read().split()
    word_pair_counts = {}
    for i in range(len(words) - 1):
        pair = ' '.join(words[i:i+2])
        if pair in word_pair_counts:
            word_pair_counts[pair] += 1
        else:
            word_pair_counts[pair] = 1
    return word_pair_counts


def get_max_count(word_pair_counts):
    """Finds element of dictionary with greatest value.

    Args:
        word_pair_counts: dictionary whose values are integers

    Returns:
        Tuple of (a) list of dictionary keys with greatest value and (b)
        that greatest value
    """

    max_count = 0
    max_word_pairs = []
    for (word_pair, count) in word_pair_counts.items():
        if count == max_count:
            max_word_pairs.append(word_pair)
        elif count > max_count:
            max_count = count
            max_word_pairs = [word_pair]
    return (max_word_pairs, max_count)


def main():
    if len(sys.argv) < 2:
        error_message = 'usage: %s filename\n' % (sys.argv[0],)
        sys.stderr.write(error_message)
        exit(1)
    word_pair_counts = get_word_pair_counts(sys.argv[1])
    (max_word_pairs, max_count) = get_max_count(word_pair_counts)
    print max_word_pairs, max_count


if __name__ == '__main__':
    main()
