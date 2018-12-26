#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n = n-1
    multiples_5 = 5*(n//5)*(n//5+1)//2
    multiples_3 = 3*(n//3)*(n//3+1)//2
    multiples_15 = 15*(n//15)*(n//15+1)//2
    print(multiples_5+multiples_3-multiples_15)
