#!/bin/python3

import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prime_set = set()
    for i in range(math.ceil(math.sqrt(n)+1)):
        if i>1:
            if n%i==0:
                is_prime = True
                for prime in prime_set:
                    if i%prime==0:
                        is_prime = False
                if is_prime:
                    prime_set.add(i)
                    
    for i in reversed(range(math.ceil(math.sqrt(n))+1)):
        if i>1:
            if n%i==0:
                complement = n//i
                is_prime = True
                for prime in prime_set:
                    if complement%prime==0:
                        is_prime = False
                if is_prime:
                    prime_set.add(complement)
    if len(prime_set)==0:
        prime_set.add(n)
    print(max(prime_set))
