# question : https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#
from itertools import product

def countSwaps(a):
    # Write your code here
    numberOfSwaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]> a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                numberOfSwaps+=1
    print("Array is sorted in %s swaps." %numberOfSwaps)
    print("First Element: %s" %a[0])
    print("Last Element: %s" %a[-1])
if __name__ == '__main__':
    n = int(raw_input().strip())

    a = map(int, raw_input().rstrip().split())

    countSwaps(a)
