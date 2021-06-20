from collections import Counter
total = 0
for line in open("input.txt","r").readlines():
    cond,passw = line.split(": ")
    min_ = int(cond.split(" ")[0].split("-")[0])
    max_ = int(cond.split(" ")[0].split("-")[1])
    letter = cond.split(" ")[1]
    count = Counter(passw)
    if letter in count and count[letter]>=min_ and count[letter]<=max_:
        total+=1
print(total)
