from collections import Counter
count = 0
for i in range(123257,647015 + 1):
    array = [int(x) for x in str(i)]
    if array[0]<=array[1] and array[1]<=array[2] and array[2]<=array[3] and array[3]<=array[4] and array[4]<=array[5]:
        counter = Counter(array)
        if len(set(array))<6:
            counter  = Counter(array)
            if 2 in counter.values():
                count+=1
print(count)
