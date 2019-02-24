#!/bin/python3

import math
import os
import random
import re
import sys

def sum_digits(n):
    sum_ = 0
    my_n = n
    while my_n!=0:
        sum_+=my_n%10
        my_n = my_n//10
    return sum_

def superDigit(n, k):
    first_sum = k*sum_digits(n)
    while first_sum%10!=first_sum:
        first_sum = sum_digits(first_sum)
    return first_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

