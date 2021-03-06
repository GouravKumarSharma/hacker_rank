#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
# This is hackerrank problem under Data Structure.

def diagonalDifference(arr,n):
    # Write your code here
    principal = 0
    secondary = 0

    rs=0
    for i in range(0, n):
        principal += arr[i][i]
        secondary += arr[i][n-i-1]
    rs=principal-secondary
    return abs(rs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,3)

    fptr.write(str(result) + '\n')

    fptr.close()
