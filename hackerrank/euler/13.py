t = int(input().strip())
numbers = []
for a0 in range(t):
    numbers.append(int(input().strip()))
suma = sum(numbers)
print(int(str(suma)[0:10]))
