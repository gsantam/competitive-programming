#!/bin/python3

import sys
import math
triangles = [-1 for x in range(3000*3)]

for a in range(1,3000):
    for b in range(1,a):
        c = math.sqrt(a**2 + b**2)
        if c<=3000:
            if int(c) == c:
                c = int(c)
                triangles[a+b+c] = max(triangles[a+b+c],a*b*c)
            
            

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(triangles[n])
