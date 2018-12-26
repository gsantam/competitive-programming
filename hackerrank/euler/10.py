##### !/bin/python3

import sys
import math

t = int(input().strip())
prime_list = list()
cribe = [True for x in range(10**6+1)]
results = []
results.append(0)
results.append(0)

max_result = 1
for a0 in range(t):
    n = int(input().strip())
    offset = max_result + 1
    if n>max_result:
        for prime in prime_list:
            max_mult = math.floor(max_result/prime)
            while max_mult*prime <=n:
                cribe[int(max_mult*prime)] = False
                max_mult+=1

        for i in range(offset,n+1):
            results.append(results[i-1])
            if cribe[i] == True:
                prime_list.append(i)
                results[i]+= i
                mult = 2
                while mult*i <= n:
                    cribe[mult*i] = False
                    mult+=1
        
    if n>max_result:
        max_result = n
        
    print(results[n])
