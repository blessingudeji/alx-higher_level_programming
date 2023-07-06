#!/usr/bin/python3
"""the function module that adds or sums integers"""


def add_integer(a, b=98):
    """Returns the sum of two integers.

    Raises:
    - TypeError: If none is an int or a float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
