import numpy as np
import sys
import doctest
from arc_utils import read_json, read_input_samples


translations_dict = {1: 5, 2: 6, 3: 4, 4: 3, 5: 1, 6: 2, 8: 9, 9: 8}


def process_value(v):
    """
    Function to process/transform the cells in the input values to the correct output values
    :param v: current cell value to process
    :return: processed/transformed output value

    >>> process_value(1)
    5
    >>> process_value(9)
    8
    >>> process_value(7)
    Traceback (most recent call last):
        ...
    KeyError: 7
    """
    return translations_dict[v]


def solve(input_grid):
    """
    solve is the function called to transform the input values into the expected output values
    :param input_grid: a single input grid from the list of grids
    :return:tuple - original input grid and transformed output grid

    >>> test_input_grid = [[9, 3, 8, 2], [3, 4, 6, 9]]
    >>> solve(test_input_grid)
    ([[9, 3, 8, 2], [3, 4, 6, 9]], array([[8, 4, 9, 6],
           [4, 3, 2, 8]]))
    >>> test_input_grid = [[1, 3, 5, 3], [1, 8, 9, 3]]
    >>> solve(test_input_grid)
    ([[1, 3, 5, 3], [1, 8, 9, 3]], array([[5, 4, 1, 4],
           [5, 9, 8, 4]]))
    """
    numpy_grid = np.array(input_grid)
    output_grid = np.zeros(numpy_grid.shape, dtype=int)
    for (x,y), value in np.ndenumerate(numpy_grid):
        output_grid[x][y] = process_value(value)

    return input_grid, output_grid


def main(args):
    """
    Main method, executed from command line
    :param args: json file with puzzle to solve
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