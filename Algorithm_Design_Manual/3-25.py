#!/usr/bin/python -tt

"""O(n+m) (where 'n' is size of text and 'm' is size of search string) time
solution to problem 3-25 from /The Algorithm Design Manual/, 2nd ed., by Steven
Skiena
"""

import sys


def add_to_count(search_string):
    """Counts occurrences of each character in specified string.

    Args:
        search_string: string whose characters to count

    Returns:
        Dictionary mapping characters in search string to the number of times
        (integer) they appear
    """

    counts = {}
    for character in search_string:
        if character not in counts:
            counts[character] = 1
        else:
            counts[character] += 1
    return counts


def subtract_from_count(counts, magazine_string):
    """Determines whether text of magazine contains sufficient occurrences of
    set of characters to compose certain string.

    Args:
        counts: dictionary mapping characters in string to compose to the
                number of times they appear in string
        magazine_string: string representing characters in magazine
    """

    # Approach: 'counts' contains characters we need and their number; iterate
    # over magazine text and decrement respective count whenever we encounter
    # a character we need; stop early when we have them all
    for character in magazine_string:
        if character in counts:
            if counts[character] == 1:
                del counts[character]
                if len(counts) == 0:
                    return True
            else:
                counts[character] -= 1
    return False


def main():
    if len(sys.argv) < 3:
        err = 'usage: %s search_string magazine_text_file\n' % (sys.argv[0],)
        sys.stderr.write(err)
        exit(1)
    counts = add_to_count(sys.argv[1])
    with open(sys.argv[2], 'rU') as file_in:
        text = file_in.read()
    print subtract_from_count(counts, text)


if __name__ == '__main__':
    main()
