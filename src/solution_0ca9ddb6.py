# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:53:58 2019

@author: Joe
"""

from arc_utils import read_json, read_input_samples
import doctest
import numpy as np
import sys


def handle_blue_occurrence(numpy_grid, x_pos, y_pos):
    """
    Function that handles the occurrence of finding a "blue" square in the input grid. Processes the grid and adds
    a orange square in set positions around it
    :param numpy_grid: The input grid
    :param x_pos: x position where the blue square was found
    :param y_pos: y position where the blue square was found
    :return: numpy_grid: containing correct output for single input grid
    """
    numpy_grid[x_pos-1, y_pos] = 7
    numpy_grid[x_pos+1, y_pos] = 7
    numpy_grid[x_pos, y_pos+1] = 7
    numpy_grid[x_pos, y_pos-1] = 7

    return numpy_grid


def handle_red_occurrence(numpy_grid, x_pos, y_pos):
    """
    Function that handles the occurrence of finding a "red" square in the input grid. Processes the grid and adds
    a yellow square in set positions around it
    :param numpy_grid: The input grid
    :param x_pos: x position where the red square was found
    :param y_pos: y position where the red square was found
    :return: numpy_grid: containing correct output for single input grid
    """
    numpy_grid[x_pos-1, y_pos-1] = 4
    numpy_grid[x_pos-1, y_pos+1] = 4
    numpy_grid[x_pos+1, y_pos-1] = 4
    numpy_grid[x_pos+1, y_pos+1] = 4

    return numpy_grid


def solve(input_grid):
    """
    solve is the function called to transform the input values into the expected output values
    :param input_grid: a single input grid from the list of grids
    :return: output_grid: a single output grid in numpy format after processing.
    """
    numpy_grid = np.array(input_grid)
    
    for ix, iy in np.ndindex(numpy_grid.shape):
        if numpy_grid[ix, iy] == 1:
            output_grid = handle_blue_occurrence(numpy_grid, ix, iy)
            
        elif numpy_grid[ix, iy] == 2:
            output_grid = handle_red_occurrence(numpy_grid, ix, iy)
    
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
