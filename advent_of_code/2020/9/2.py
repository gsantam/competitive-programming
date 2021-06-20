target = 1639024365
numbers  = [int(number) for number in open("input.txt","r").readlines() if number!="\n"]
cum_numbers = [0 for i in range(len(numbers)+1)]
for i,number in enumerate(numbers):
    cum_numbers[i+1] = cum_numbers[i]+number
i = 0
j = 0
while not (cum_numbers[j]-cum_numbers[i]==target and j>i+1):
    if j==len(cum_numbers)-1 or cum_numbers[j]-cum_numbers[i]>target:
        i+=1
    else:
        j+=1
print(max(numbers[i:j])+min(numbers[i:j]))
