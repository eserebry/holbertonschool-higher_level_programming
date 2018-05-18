#!/usr/bin/python3
def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    Args:
        n - size of triangle
    """
    outer = []

    for i in range(n):
        inner = []
        for j in range(i + 1):
            if j == 0 or j == i:
                inner.append(1)
            else:
                inner.append(outer[i-1][j-1] + outer[i-1][j])
        outer.append(inner)
    return outer
