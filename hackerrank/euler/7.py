##### !/bin/python3

import sys
import math

#t = int(input().strip())
prime_list = list()
MAX = 105000
cribe = [True for x in range(MAX)]

for i in range(2,MAX):
    if cribe[i]:
        prime_list.append(i)
        mult = 2
        while i*mult < MAX:
            cribe[i*mult] = False
            mult+=1

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(prime_list[n-1])
