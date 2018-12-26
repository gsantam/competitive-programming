#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    visited_primes = []
    number = 1
    for i in range(n+1):
        if i>0:
            remainder = i
            for j in visited_primes:
                if remainder%j == 0:
                    remainder = remainder // j
            visited_primes.append(remainder)
            number*=remainder
    print(number)
                    
                    
