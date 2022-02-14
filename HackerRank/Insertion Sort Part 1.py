#question https://www.hackerrank.com/challenges/insertionsort1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    end = arr[-1]
    idx = n-2

    while (end < arr[idx]) and (idx >= 0):
        arr[idx+1] = arr[idx]
        print(*arr)
        idx -= 1

    arr[idx+1] = end
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
