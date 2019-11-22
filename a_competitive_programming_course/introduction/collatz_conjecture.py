def collatz(n):
    if n%2 == 0 :
        return n // 2
    else:
        return 3*n+1

while True:
    n, m = [int(x) for x in input().split(" ")]
    or_n = n
    or_m = m
    if n == 0 and m == 0:
        break
    
    visited = {}
    visited[n] = 0
    i = 1
    while n!=1:
        n = collatz(n)
        visited[n] =i
        i+=1
    found = False
    i = 0
    while not found:
        if m in visited:
            found = True
        else:
            m = collatz(m)
            i+=1
            
    print(str(or_n)+" needs "+str(visited[m])+" steps, "+str(or_m)+" needs "+str(i)+" steps, they meet at "+str(m))
    
