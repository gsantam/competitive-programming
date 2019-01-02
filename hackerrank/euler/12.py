import time

length_cribe = 10**5
eratostenes_cribe = [[] for x in range (length_cribe)]
for i in range(2,length_cribe):
    #eratostenes_cribe[i].append(i)
    if len(eratostenes_cribe[i])==0:
        mult = 2
        while i*mult <length_cribe:
            j = i*mult
            eratostenes_cribe[j].append(i)
            mult+=1
            
import math

def get_number_divisors(number):
    my_primes = eratostenes_cribe[number]
    divisors = [number,1]
    my_divisors = set(divisors)

    while len(divisors)>0:
        divisor = divisors.pop()
        for prime in my_primes:
            if divisor%prime==0:
                my_divisors.add(divisor//prime)
                divisors.append(divisor//prime)
                
    return my_divisors


max_number = 0
n = 50000
max_numbers = [0 for i in range(2000)]


for i in range(n):
    if i%2==0:
        number_divisors_n =  get_number_divisors(i//2)
        number_divisors_n_p_1 =  get_number_divisors(i+1)
    else:
        number_divisors_n =  get_number_divisors(i)
        number_divisors_n_p_1 =  get_number_divisors((i+1)//2)
    my_divisors = set()
    for j in number_divisors_n:
        for k in number_divisors_n_p_1:
            my_divisors.add(j*k)
    if len(my_divisors)>max_number:
        for j in range(max_number+1,len(my_divisors)):
            max_numbers[j] = (i*(i+1))//2
        max_number = len(my_divisors) - 1
        
max_numbers[1] = 3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(max_numbers[n])
