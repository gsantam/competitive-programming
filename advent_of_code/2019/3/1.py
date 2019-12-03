paths = open("input.txt","r").read().split("\n")
path_0 = paths[0].split(",")
path_1 = paths[1].split(",")
next_ = (0,0)
sequence = set()

for element in path_0:
    n = int(element[1:])
    direction = element[0]
    for i in range(n):
        if direction == "R":
            next_ = (next_[0]+1,next_[1])
        elif direction == "L":
            next_ = (next_[0]-1,next_[1])
        elif direction == "U":
            next_ = (next_[0],next_[1]+1)
        else:
            next_ = (next_[0],next_[1]-1)
        sequence.add(next_)

coincidences = {}

next_ = (0,0)
for element in path_1:
    n = int(element[1:])
    direction = element[0]
    for i in range(n):
        if direction == "R":
            next_ = (next_[0]+1,next_[1])
        elif direction == "L":
            next_ = (next_[0]-1,next_[1])
        elif direction == "U":
            next_ = (next_[0],next_[1]+1)
        else:
            next_ = (next_[0],next_[1]-1)
        if next_ in sequence:
            coincidences[next_] = abs(next_[0])+abs(next_[1])

print(min(coincidences.values()))
