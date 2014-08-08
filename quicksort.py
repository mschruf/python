"""Implements Quicksort algorithm.
"""

import random # for random selection of pivot element


def swap_elements(mut_seq, index1, index2):
    """Swaps two elements of mutable sequence.

    Args:
        mut_seq: mutable sequence
        index1: index of element to be swapped with element with index 'index2'
        index2: index of element to be swapped with element with index 'index1'

    Returns:
        Nothing
    """

    if index1 == index2:
        return
    temp = mut_seq[index1]
    mut_seq[index1] = mut_seq[index2]
    mut_seq[index2] = temp


def quicksort(mut_seq, index_start, index_end):
    """Sorts mutable sequence in place using Quicksort algorithm.

    Args:
        mut_seq: mutable sequence to be sorted
        index_start: index of first element of l to be sorted
        index_end: index of last element of l to be sorted

    Returns:
        Nothing

    Raises:
        IndexError: if argument 'index_end' exceeds greatest valid index for
                    argument 'l'
    """

    if index_end >= len(mut_seq):
        raise IndexError
    if index_end - index_start < 1:
        return

    pivot_index = random.randrange(index_start, index_end + 1)
    # temporarily move pivot element out of way at end of array
    swap_elements(mut_seq, pivot_index, index_end)
    pivot_index = index_end

    # partition
    swappable_index = index_start
    for i in range(index_start, index_end):
        if mut_seq[i] < mut_seq[pivot_index]:
            swap_elements(mut_seq, i, swappable_index)
            swappable_index += 1

    # move pivot to its final place in sorted order
    swap_elements(mut_seq, swappable_index, pivot_index)
    pivot_index = swappable_index

    # now sort subsequence to left and right of pivot element
    quicksort(mut_seq, index_start, pivot_index - 1)
    quicksort(mut_seq, pivot_index + 1, index_end)
