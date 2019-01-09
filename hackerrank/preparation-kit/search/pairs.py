#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    visited_numbers = dict()
    counts = 0
    for element in arr:
        if k+element in visited_numbers:
            counts+=visited_numbers[k+element]
        if element-k in visited_numbers:
            counts+=visited_numbers[element-k]
        if element not in visited_numbers:
            visited_numbers[element] = 0
        visited_numbers[element]+=1
    return counts
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

