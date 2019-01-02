#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
# Complete the countingValleys function below.
def countingValleys(n, s):
    n = 0
    accu = 0
    for i in list(s):
        if i=="D":
            accu-=1

        else:
            accu+=1
            if accu==0:
                n+=1

    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

