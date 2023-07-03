#!/usr/bin/python3

"""defines a function that prints a square"""
def print_square(size):
    """
    prints a square with #

    Args:
        size(int): length of the square

    Raise:
        TypeError: if size not integer or float
        ValueError: if size less than zero
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for _ in range(size):
        print("#" * size)
