cases = int(input())
for i in range(cases):
    m,r = input().split(" ")
    m = int(m)
    r = int(r)
    stack = [m - i  for i in range(m)]
    solution = []
    numbers = [int(x) for x in input().split(" ")]
    for j in range(r):
        number = numbers[j]
        for k in range(len(stack)):
            if stack[len(stack) - k -1 ] == number:
                solution.append(k)
                del stack[len(stack) - k -1 ]
                break
        stack.append(number)
    print(" ".join([str(x) for x in solution]))   
