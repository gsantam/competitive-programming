#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    minimum_difference = abs(arr[1] - arr[0])
    for i, num in enumerate(arr):
        if i > 1:
            minimum_difference = min(minimum_difference,abs(arr[i] - arr[i-1]))
    return minimum_difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

