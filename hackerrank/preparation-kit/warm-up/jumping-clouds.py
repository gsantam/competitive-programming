#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    cloud = 0
    num = 0
    while cloud < len(c) - 1:
        num+=1
        if cloud+2 <len(c) and c[cloud+2] == 0:
            cloud+=2
        else:
             cloud+=1
    return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

