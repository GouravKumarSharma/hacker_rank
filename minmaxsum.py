#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sums = tuple(sum(arr[:i] + arr[i + 1:]) for i in range(len(arr)))
    print('%i %i' % (min(sums), max(sums)))
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
