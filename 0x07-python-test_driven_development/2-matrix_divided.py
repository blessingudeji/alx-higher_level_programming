#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides each element in a matrix by a div..

    Args:
        matrix: A list of lists to be divided.
        div(int or float: The divisor.

    Returns:
        A new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists,
                   or if div is not a number.
        TypeError: If rows of the matrix does not have the same size.
        ZeroDivisionError: If div == 0.
    """

    if not all(
            isinstance(row, list) and
            all(isinstance(num, (int, float)) for num in row)
            for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = set(len(row) for row in matrix)
    if len(row_sizes) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
