import math
while True:
    numbers = [int(x) for x in input().split(" ")]
    if numbers[0] == 0:
        break
    n = numbers[0]
    perm = numbers[1:]
    message = input()
    encripted_message = ""
    for i in range((math.ceil(len(message) / n))) :
        for j in range(n):
            if i*(n) + perm[j]-1 < len(message):
                encripted_message+=message[i*(n) + perm[j] -1]
            else:
                encripted_message+=" "
    print("'"+encripted_message+"'")
