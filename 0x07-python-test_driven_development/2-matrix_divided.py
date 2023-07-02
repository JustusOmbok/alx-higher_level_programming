#!/usr/bin/python3

"""Defines a function that divides a matrix"""

def matrix_divided(matrix, div):
    """
    divide all elements of a mtrix by a given number

    Args:
        matrix (list): a list of lists representing the mrix
        div (int or float): the number to divide the elements of the matrix by
    Returns:
        list: a new matrix with elements divided by div, rounde to 2 decimal places
    Raises:
        TypeError: If the matrix is not a list of integers or floats
        Typeerror: if each row of the matrix is not equal
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is equal to 0

"""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a mtrix (list of lists) of integer/floats")

    row_sizes = [len(row) for row in matrix]
    if not all(size == row_sizes[0] for size in row_sizes):
        raise TypeError("Each row of the matrix must havethe same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
