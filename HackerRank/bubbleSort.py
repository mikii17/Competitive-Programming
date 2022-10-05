#!/bin/python3

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

def countSwaps(a):
    # Write your code here
    counter = 0
    for i in range(len(a) - 1):
        for j in range(1, len(a) - i):
            if a[j] < a[j - 1]:
                counter += 1
                a[j], a[j - 1] = a[j - 1], a[j]
    print("Array is sorted in {:d} swaps.".format(counter))
    print("First Element: {:d}".format(a[0]))
    print("Last Element: {:d}".format(a[len(a) - 1]))
        
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
