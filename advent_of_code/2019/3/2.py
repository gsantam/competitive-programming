paths = open("input.txt","r").read().split("\n")
path_0 = paths[0].split(",")
path_1 = paths[1].split(",")
next_ = (0,0)
sequence = {}

time = 0
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
        time+=1
        if next_ not in sequence: 
            sequence[next_]=time

coincidences = {}
next_ = (0,0)
time = 0
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
        time+=1
        if next_ in sequence and next_ not in coincidences:
            coincidences[next_] = sequence[next_] + time

print(min(coincidences.values()))
