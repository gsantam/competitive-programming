from collections import Counter
total = 0
for line in open("input.txt","r").readlines():
    cond,passw = line.split(": ")
    min_ = int(cond.split(" ")[0].split("-")[0])
    max_ = int(cond.split(" ")[0].split("-")[1])
    letter = cond.split(" ")[1]
    letters = set([passw[min_-1],passw[max_-1]])
    if len(letters)==2 and letter in letters:
        total+=1

print(total)
