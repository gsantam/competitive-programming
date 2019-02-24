#!/bin/python3

import math
import os
import random
import re
import sys

def stepPerms(n):
    cached_results = [0 for x in range(37)]
    cached_results[1] = 1
    cached_results[2] = 2
    cached_results[3] = 4
    for i in range(4,37):
        cached_results[i] = cached_results[i-1] + cached_results[i-2]+ cached_results[i-3]
    return cached_results[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())
    cached_results = dict()
    for s_itr in range(s):
        n = int(input())
        if n in cached_results:
            res = cached_results[n]
        else:
            res = stepPerms(n)
            cached_results[n] = res

        fptr.write(str(res) + '\n')

    fptr.close()

