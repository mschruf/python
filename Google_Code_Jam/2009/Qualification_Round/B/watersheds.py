#!/usr/bin/python -tt

"""Solves Google Code Jam 2009 Qualification Round Problem B
(https://code.google.com/codejam/contest/90101/dashboard#s=p1)
"Watersheds"
"""

import sys


def read_input():
    """Parses problem input data from stdin.

    Args:
        None

    Returns:
        List of test cases, where each test case is map of altitudes as 'height'
        lists of 'width' integers, such that test_case[row][column] represents
        altitude of cell with coordinates (row, column)
        
    Raises:
        AssertionError: on invalid input
    """

    lines = sys.stdin.read().splitlines()
    num_test_cases = int(lines[0])
    i = 1
    test_cases = []
    for _ in range(num_test_cases):
        (height, width) = [int(x) for x in lines[i].split()]
        i += 1
        map_altitudes = []
        for k in range(height):
            altitude_row = [int(x) for x in lines[i + k].split()]
            assert len(altitude_row) == width
            map_altitudes.append(altitude_row)
        assert len(map_altitudes) == height
        i += height
        test_cases.append(map_altitudes)
    return test_cases


def label_map(map_labels, children, cell_starting, label):
    """Labels specified cell and all cells which drain into it with specified
    label on watershed basin map.

    Args:
        map_labels: map of cells to be modified as requested; same data
            structure as 'altitudes' map, but each element is string
            representing watershed basin label rather than integer representing
            altitude
        children: dict mapping cell to list of cells which drain into it; cell
            represented by zero-index (row, column) tuple
        cell_starting: (row, column) tuple identifying cell with which to
            start labelling process (i.e. label it and all its upstream cells)
        label: string representing label to assign to specified cells

    Returns:
        None
    """

    (row, column) = cell_starting
    map_labels[row][column] = label
    if cell_starting in children:
        for cell in children[cell_starting]:
            label_map(map_labels, children, cell, label)


def get_map_labels(map_height, map_width, children):
    """Given dimensions of map and tree of cells with sinks as roots, label
    each cell with watershed basin to which it belongs.

    Args:
        map_height: height of map
        map_width: width of map
        children: dict mapping cell to list of cells which drain into it; cells
            represented by zero-index (row, column) tuple

    Returns:
        Map with labels; data structure same as 'altitudes' map specifying
            test case, but with label string elements rather than altitude
            integers
    """

    # NOTE: we don't have sufficient information at this point to assign
    # labels so that they adhere to the label ordering specified by the problem;
    # so we'll assign temporary labels and use upper-case letters to distinguish
    # them from final labels during later relabeling

    first_label = 'A'

    # create empty label map
    map_labels = [[str() for _ in range(map_width)] for _ in range(map_height)]

    label = first_label
    for cell_sink in children[None]:
        label_map(map_labels, children, cell_sink, label)
        label = chr(ord(label) + 1)
    return map_labels


def get_cell_neighbors(cell, map_height, map_width):
    """Yields N, W, E, and S neighbors of specified cell given constraints of
    map dimensions.

    Args:
        cell: coordinates of cell whose neighbors we want as (row, column)
              tuple; row and column numbers are zero-based

    Yields:
        (row, column) tuple representing neighbors of specified cell; row and
        column numbers are zero-based
    """

    (row, column) = cell
    # NOTE: we return neighbors in order N, W, E, S so that, as a side-effect of
    # the algorithm in get_drain() for finding neighbor with minimum altitude,
    # any ties are broken according to rule specified in problem
    if row > 0: yield (row - 1, column)
    if column > 0: yield (row, column - 1)
    if column + 1 < map_width: yield (row, column + 1)
    if row + 1 < map_height: yield (row + 1, column)


def get_cell_drain(map_altitudes, cell):
    """Identifies cell into which specified cell drains.

    Args:
        map_altitudes: map of cells and their altitude; list of 'height' lists
            with 'width' integers each, so that 'altitudes[row][column]' is
            altitude of cell with coordinates (row, column)
        cell: cell, as tuple of (row, column) coordinates, whose drainage cell
            to identify

    Returns:
        - (row, column) tuple identifying cell into which cell specified in
          arguments drains
        - None if specified cell is sink
    """

    map_height = len(map_altitudes)
    map_width = len(map_altitudes[0])
    altitude_min = map_altitudes[cell[0]][cell[1]]
    cell_altitude_min = cell
    for cell_neighbor in get_cell_neighbors(cell, map_height, map_width):
        altitude_neighbor = map_altitudes[cell_neighbor[0]][cell_neighbor[1]]
        if altitude_neighbor < altitude_min:
            altitude_min = altitude_neighbor
            cell_altitude_min = cell_neighbor
    return cell_altitude_min if cell_altitude_min != cell else None


def fix_labels(map_labels):
    """Changes watershed basin labels to adhere to ordering specified in
    problem.

    Args:
        map_labels: map of watershed basin labels to be changed; same data
            structure as 'altitudes' map, but elements are string representing
            cell watershed basin rather than integers representing cell altitude

    Returns:
        None
    """

    # make mapping of old-label --> new-label
    # approach: iterate over cells in order of row, then column and assign
    # increasing label IDs ('a', 'b', 'c', ...) to current labels as discovered,
    # i.e. first label we encounter, gets new label 'a', next heretofore-unseen
    # label gets new label 'b', etc.
    label_new = 'a'
    new_labels = {}
    map_height = len(map_labels)
    map_width = len(map_labels[0])
    for row in range(map_height):
        for column in range(map_width):
            label_old = map_labels[row][column]
            if label_old not in new_labels:
                assert ord(label_new) <= ord('z')
                new_labels[label_old] = label_new
                label_new = chr(ord(label_new) + 1)
    # relabel map using old-label --> new-label mapping
    for row in range(map_height):
        for column in range(map_width):
            map_labels[row][column] = new_labels[map_labels[row][column]]


def solve(map_altitudes):
    """Create map of cell watershed basins from map of cell altitudes.

    Args:
        map_altitudes: map of cells and their altitude; list of 'height' lists
            with 'width' integers each, so that 'altitudes[row][column]' is
            altitude of cell with coordinates (row, column)

    Returns:
        Same data structure as argument, but with watershed basin label strings
        as data rather than altitude integers
    """

    # create trees where root is sink cell and each node's children are those
    # cells which drain into it; representing tree as dict, where
    # 'children[cell]' is list of cells which drain into cell 'cell';
    # essentially representing tree by edges and list of root nodes
    map_height = len(map_altitudes)
    map_width = len(map_altitudes[0])
    children = {}
    for row in range(map_height):
        for column in range(map_width):
            cell = (row, column)
            cell_drain = get_cell_drain(map_altitudes, cell)
            if cell_drain in children:
                children[cell_drain].append(cell)
            else:
                children[cell_drain] = [cell]
    basin_labels = get_map_labels(map_height, map_width, children)
    fix_labels(basin_labels)
    return basin_labels


def main():
    test_cases = read_input()
    i = 1
    for test_case in test_cases:
        print 'Case #%d:' % (i,)
        map_basin_labels = solve(test_case)
        for map_row in map_basin_labels:
            print ' '.join(map_row)
        i += 1


if __name__ == '__main__':
    main()
