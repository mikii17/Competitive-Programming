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
def printer(n, arr):
    for i in range(n):
        print(arr[i], end="")
        if i != (n - 1):
            print(" ", end="")

def insertionSort1(n, arr):
    # Write your code here
    key = arr[n - 1]
    n = n - 2
    while n >= 0 and key < arr[n]:
        arr[n + 1] = arr[n]
        n -= 1
        printer(n, arr)
        print()
    arr[n + 1] = key
    printer(n, arr)
         

        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
