#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    previous_visits = dict()
    counts = 0
    
    for num in arr:
        prev_triplet = num/r
        if prev_triplet in previous_visits:
            prev_tiplet_count=previous_visits[prev_triplet][0]
            counts+=previous_visits[prev_triplet][1]
        else:
            prev_tiplet_count=0
            
        if num not in previous_visits:
            previous_visits[num]=[0,0]
        previous_visits[num][0]+=1
        previous_visits[num][1]+=prev_tiplet_count
        
        
    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

