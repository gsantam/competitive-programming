numbers = [int(x) for x in open("input.txt","r").read().strip().split(",")]
numbers[1] = 12
numbers[2] = 2
for i in range(int(len(numbers)/4)):
    j = 4*i
    actual = numbers[j]
    if actual == 99:
        break
    if actual == 1:
        numbers[numbers[j+3]] = numbers[numbers[j+1]]+ numbers[numbers[j+2]]
    else:
        numbers[numbers[j+3]] = numbers[numbers[j+1]]*numbers[numbers[j+2]]
print(numbers[0])
