n = 0
letters = set()
sums = 0
for line in open("input.txt","r").readlines():
    if line == "\n":
        n = 0
        sums+=len(letters)
        letters = set()
    else:
        letters = letters.union(set([x for x in line.strip()]))
        n+=1
        
sums+=len(letters)
print(sums)
