#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_hg = -999999
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i>=1 and j>=1 and i<len(arr)-1 and j < len(arr[0]) -1 :
                h_glass = sum(arr[i-1][j-1:j+2]) + sum(arr[i+1][j-1:j+2]) + arr[i][j]
                max_hg = max(max_hg,h_glass)
    return max_hg

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

