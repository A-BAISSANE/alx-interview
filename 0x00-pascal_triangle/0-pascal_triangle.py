#!/usr/bin/env python3
from typing import List

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


# Testing the function
if __name__ == "__main__":
    pascal_result = pascal_triangle(5)
    for row in pascal_result:
        print(row)
