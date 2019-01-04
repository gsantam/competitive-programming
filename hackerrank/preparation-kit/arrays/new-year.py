import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    ordered_position = [0 for x in range(len(q))]
    for i, pos in enumerate(q):
        pos_ = pos - 1
        if pos_ > i +2 :
            return "Too chaotic" 
        ordered_position[pos_] = i
        
    for number in range(len(q)):
        pos_ = ordered_position[number]
        j = pos_
        while number>j:
            tmp = q[j+1]
            q[j+1] = q[j]
            q[j] = tmp
            ordered_position[q[j+1]-1] =j+1
            ordered_position[q[j]-1] =j
            j+=1
            
            
        while number<j:
            tmp = q[j-1]
            q[j-1] = q[j]
            q[j] = tmp
            ordered_position[q[j-1]-1] =j+1
            ordered_position[q[j]-1] =j
            j-=1
            bribes+=1
    return bribes



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))


