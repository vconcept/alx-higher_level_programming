#!/usr/bin/python3
def matrix_divided(matrix):
    for i in matrix:
        temp0 = 0
        temp1 = 1
        for j in i:
            if not isinstance(i, list) or not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        while len(i[temp0]) != len(i[temp1]):
            raise TypeError("Each row of the matrix must have the same size")
            temp0 += 1
            temp1 += 1
    return

mat1 = [[1,3,5], [1,6,9], [8,2,5]]
matrix_divided(mat1)

#!/usr/bin/python3
"""
This module is composed by a function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix
    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix
    Returns:
        A new matrix with the result of the division
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
