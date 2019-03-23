import math
t = int(input())
for i in range(t):
    a, b = [int(x) for x in input().split(" ")]
    n = int(input())
    i = 0
    found = False
    left = a
    right = b
    while i < n and not found:
        number = math.ceil((left + right) / 2)
        print(number)
        s = input()
        if s == "TOO_BIG":
            right = number
        elif s == "TOO_SMALL":
            left = number
        elif s == "CORRECT":
            found = True
        i+=1
