"""
n1 = 7 n2 = 4

n2 = 3
n1 = -3 +7 = 4
n2 = 3 + 4 = 7

"""

def swap_numbers(n1,n2):
    if n1==n2:
        return n1,n2
    
    n2 = n1 - n2
    n1 = -n2 + n1
    
    n2 = n2 +n1
    
    return n1,n2


print(swap_numbers(1900,-10))
    
    
