t1 = open("testdata/plaintexts/test1.txt", 'rb').read()
t2 = open("testdata/plaintexts/test2.txt", 'rb').read()
ct1 = open("testdata/ciphered/test1.txt",'rb').read()
ct2 = open("testdata/ciphered/test2.txt", 'rb').read()

t1n = int(t1.hex(),16)
t2n = int(t2.hex(),16)

ct1n = int(ct1.hex(),16)
ct2n = int(ct2.hex(),16)

import math

e = 65537

exp_t1n = t1n**e
exp_t2n = t2n**e
print(math.gcd(exp_t1n - ct1n,exp_t2n - ct2n))
