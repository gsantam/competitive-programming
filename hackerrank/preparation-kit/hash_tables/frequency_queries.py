#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    num_rep = dict()
    freq = dict()
    freq[0] = 0
    sol_array = list()
    for query in queries:
        op = query[0]
        num = query[1]
        if op==1:
            if num not in num_rep:
                num_rep[num] = 0
            num_rep[num]+=1
            num_freq = num_rep[num]
            if num_freq not in freq:
                freq[num_freq] = 0
            freq[num_freq] +=1
            freq[num_freq-1] -=1
        
        if op==2:
            if num in num_rep and num_rep[num]>0:
                num_rep[num]-=1
                num_freq = num_rep[num]
                if num_freq not in freq:
                    freq[num_freq] = 0
                freq[num_freq] +=1
                freq[num_freq+1] -=1

        if op==3:
            if num in freq and freq[num]>0:
                sol_array.append(1)
            else:
                sol_array.append(0)
    return sol_array



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

