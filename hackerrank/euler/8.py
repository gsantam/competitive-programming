#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    num = [int(x) for x in num]
    l = k
    actual_product = 1
    max_num = 0
    number_of_zeros = 0
    for idx,i in enumerate(num):
        l-=1
        if i!=0:
            actual_product*=i
        else:
            number_of_zeros+=1
        if l<=0:
            if l<0:
                if num[idx-k]!=0:
                    actual_product//=num[idx-k]
                else:
                    number_of_zeros-=1
            if actual_product>=max_num and number_of_zeros==0:
                max_num = actual_product
    print(max_num)
            

