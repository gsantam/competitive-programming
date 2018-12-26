#!/bin/python3

import sys

sum_ = 0
sum_squared = 0
results = list()
results.append(0)

for i in range(1,10001):
    sum_ = sum_ + i
    sum_squared = sum_squared+i**2
    results.append(sum_**2 - sum_squared)
    
    


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(results[n])
