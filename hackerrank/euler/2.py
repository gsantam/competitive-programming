## !/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    value_1 = 1
    value_2 = 2
    value = 3
    sum = 2
    while value <n:
        if value%2==0:
            sum+=value
        value_old = value
        value  = value_2+ value
        value_1 = value_2
        value_2 = value_old
    print(sum)

        
        
