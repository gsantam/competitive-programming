#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    q = [x-1 for x in arr]
    bribes = 0
    ordered_position = [0 for x in range(len(q))]
    for i, pos in enumerate(q):
        ordered_position[pos] = i
        
    for number in range(len(q)):
        pos = ordered_position[number]
        if pos!=number:
            tmp = q[number]
            q[number] = number
            q[pos] = tmp
            ordered_position[number] = number 
            ordered_position[tmp] = pos
            bribes+=1
    return bribes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

