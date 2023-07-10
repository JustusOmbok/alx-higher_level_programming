#!/usr/bin/python3
"""
A custom list class
"""
class   MyList(list):
    """
    A list class that inherits list
    """
    def __init__(self):
        """object is initialized"""
        super().__init__()

    def print_sorted(self):
        """
        List is printed in ascending order

        Args:
            none

        Returns:
            nothing
        """
        sorted_list = sorted(self)
        print(sorted_list)
