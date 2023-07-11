#!/usr/bin/python3
"""A pascal triangle function."""


def pascal_triangle(n):
    """Represents pascal's triangle of n"""
    Triangle = []
    prevN = []
    for i in range(n):
        atN = [1] + [sum(prevN[ele:ele + 2]) for ele in range(len(prevN) - 1)]
        if i > 0:
            atN = atN + [1]
        Triangle.append(atN)
        prevN = atN
    return Triangle
