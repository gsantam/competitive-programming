#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    counts = 0
    a = sorted(set(a))
    b = sorted(set(b))
    c = sorted(set(c))
    
    i = 0
    j = 0
    a_less_than = 0
    c_less_than = 0
    for b_ in b:
        prev_i = i
        prev_j = j
        while i < len(a) and a[i] <= b_:
            i+=1
        while j < len(c) and c[j] <= b_:
            j+=1

        a_less_than+=(i-prev_i)
        c_less_than+=(j-prev_j)
        counts+=a_less_than*c_less_than

    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()

