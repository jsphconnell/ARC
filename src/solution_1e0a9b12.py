import numpy as np
import sys
import doctest
from arc_utils import read_json, read_input_samples


def drop_numbers(arr):
    """
    function to transform input to output.
    In the case of this puzzle to move the numbers from top rows to button rows

    :param arr: numpy array with input numbers to be processed
    :return: numpy array, transformed values. All top rows non-zero values to be move to low rows

    >>> input_array = np.array([[1, 0, 2, 0],[0, 3, 0, 4],[6, 0, 7, 0],[0, 8, 0, 9]])
    >>> drop_numbers(input_array)
    array([[0, 0, 0, 0],
           [0, 0, 0, 0],
           [1, 3, 2, 4],
           [6, 8, 7, 9]])
    """
    modified = False
    output_grid = np.copy(arr)
    for (x,y), value in np.ndenumerate(arr):
        if x < arr.shape[0]-1:
            if value > 0 and output_grid[x+1][y] == 0:
                output_grid[x+1][y] = output_grid[x][y]
                output_grid[x][y] = 0
                modified = True
    if modified:
        output_grid = drop_numbers (output_grid)
    return output_grid


def solve(input_grid):
    """
    Call solve to solve puzzle. Takes an input with the grid to transform,
    :param input_grid: input grids loaded from file
    :return: numpy array tuple. Input grid and output transformed grid

    >>> test_input_grid = [[9, 3, 8, 2], [3, 4, 6, 9]]
    >>> solve(test_input_grid)
    (array([[9, 3, 8, 2],
           [3, 4, 6, 9]]), array([[9, 3, 8, 2],
           [3, 4, 6, 9]]))
    >>> test_input_grid = [[9, 3, 8, 2], [3, 0, 6, 0]]
    >>> solve(test_input_grid)
    (array([[9, 3, 8, 2],
           [3, 0, 6, 0]]), array([[9, 0, 8, 0],
           [3, 3, 6, 2]]))
    """
    numpy_grid = np.array(input_grid)
    output_grid = drop_numbers(numpy_grid)

    return numpy_grid, output_grid

def main(args):
    """
    program entry point.
    :param args: json format input file name containing the grids to be transformed
    """
    doctest.testmod()
    input_json = read_json(args[1])
    inputs_dict = read_input_samples(input_json)
    for key in inputs_dict:
        result = solve(inputs_dict[key])
        print(result[1])
        print("\n")


if __name__ == "__main__":
    main(sys.argv)