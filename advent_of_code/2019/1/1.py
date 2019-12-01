mass = open("input.txt","r").read().split("\n")
print(sum([int(int(x)/3) - 2 for x in mass if x !='']))
