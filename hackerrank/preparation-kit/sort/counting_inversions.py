#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def mergeSort(array):
    global n_swaps
    if len(array)==1:
        return array
        
    ordered_first_half = mergeSort(array[0:len(array)//2])
    ordered_second_half = mergeSort(array[len(array)//2:])
    
    ordered_array = []
    j = 0
    k = 0
    
    while j < len(ordered_first_half) and k < len(ordered_second_half):
        
        if ordered_first_half[j] <= ordered_second_half[k]:
            ordered_array.append(ordered_first_half[j])
            j+=1
        else:
            ordered_array.append(ordered_second_half[k])
            k+=1
            n_swaps+=len(ordered_first_half)-j
            
    ordered_array = ordered_array + ordered_first_half[j:]
    ordered_array = ordered_array + ordered_second_half[k:]


    return ordered_array

def countInversions(arr):
    global n_swaps
    mergeSort(arr)
    return n_swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        global n_swaps
        n_swaps = 0
        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

