#!/usr/bin/python3
"""
a class MyInt that inherits from int
"""
class MyInt(int):
    """
    class MyInt that inherits from int
    """
    def __eq__(self, other):
        """
        __eq__ method is overridden to call the parent class's __ne__ method
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        __ne__ method is overridden to call the parent class's __eq__ method
        """
        return super().__eq__(other)
