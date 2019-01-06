#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    sums_ = [0 for x in range(n)]
    for i,query in enumerate(queries):
        sums_[query[0]-1]+=query[2]
        if query[1] < n:
            sums_[query[1]]+=-query[2]

    actual_sum = 0
    actual_max = 0
    for i in range(n):
        actual_sum+=sums_[i]
        actual_max = max(actual_max,actual_sum)

    return actual_max
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

