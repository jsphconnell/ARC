from arc_utils import read_json, read_input_samples
import doctest
import numpy as np
import sys


def handle_red_or_blue_occurrence(numpy_grid, x_pos, y_pos):
    """
    Function that handles the occurrence of finding a "red(2)" or "blue(1)" square in the input grid.
    If a Blue square is found, processes the grid and adds an orange square in set positions around it
    If a red square is found, processes the grid and adds a yellow square in set positions around it
    :param numpy_grid: The input grid
    :param x_pos: x position where the blue square was found
    :param y_pos: y position where the blue square was found
    :return: numpy_grid: containing correct output for single input grid

    >>> test_input_grid = np.array([[0, 0, 0],[0, 1, 0],[0, 0, 0]])
    >>> handle_red_or_blue_occurrence(test_input_grid, 1, 1)
    array([[0, 7, 0],
           [7, 1, 7],
           [0, 7, 0]])

    >>> test_input_grid = np.array([[0, 0, 0],[0, 2, 0],[0, 0, 0]])
    >>> handle_red_or_blue_occurrence(test_input_grid, 1, 1)
    array([[4, 0, 4],
           [0, 2, 0],
           [4, 0, 4]])

    """
    if numpy_grid[x_pos, y_pos] == 1:
        numpy_grid[x_pos - 1, y_pos] = 7
        numpy_grid[x_pos + 1, y_pos] = 7
        numpy_grid[x_pos, y_pos + 1] = 7
        numpy_grid[x_pos, y_pos - 1] = 7

    elif numpy_grid[x_pos, y_pos] == 2:
        numpy_grid[x_pos - 1, y_pos - 1] = 4
        numpy_grid[x_pos - 1, y_pos + 1] = 4
        numpy_grid[x_pos + 1, y_pos - 1] = 4
        numpy_grid[x_pos + 1, y_pos + 1] = 4

    return numpy_grid


def solve(input_grid):
    """
    solve is the function called to transform the input values into the expected output values
    :param input_grid: a single input grid from the list of grids
    :return: output_grid: a single output grid in numpy format after processing.

    >>> test_input_grid = [[0, 0, 0],[0, 2, 0],[0, 0, 0]]
    >>> solve(test_input_grid)
    array([[4, 0, 4],
           [0, 2, 0],
           [4, 0, 4]])
    """
    numpy_grid = np.array(input_grid)

    for (ix, iy), value in np.ndenumerate(numpy_grid):
        if value in [1, 2]:
            output_grid = handle_red_or_blue_occurrence(numpy_grid, ix, iy)

    return output_grid


def main(args):
    """
    Main method, executed from command line
    :param args: json file with puzzle to solve
    """
    doctest.testmod()
    input_json = read_json(args[1])
    inputs_dict = read_input_samples(input_json)

    for key in inputs_dict:
        output = solve(inputs_dict[key])
        print(output)
        print("\n")


if __name__ == "__main__":
    main(sys.argv)
