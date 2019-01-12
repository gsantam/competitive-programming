#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the minTime function below.
machines = [63, 2, 26, 59, 16, 55, 99 ,21, 98, 65]
goal = 56
def minTime(machines, goal):
    machines = sorted(machines)
    import math
    def binary_search(min_days,max_days,goal,machines): 
        if round(min_days) == round(max_days):
            return round(min_days)
        if goal <= sum([math.floor(((min_days+max_days)/2)/x) for x in machines]):
            return binary_search(min_days,(min_days+max_days)/2,goal,machines)
        else:
            return binary_search((min_days+max_days)/2,max_days,goal,machines)
    return binary_search(1,machines[0]*goal,goal,machines)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()

