bags = open("input.txt").readlines()
stack = []
graph = {}
ways = 0
for bag in bags:    
    bag = bag.replace(" contain no other bags.","")
    bag_ = bag.split(" ")
    graph[tuple(bag_[:2])] = [tuple(bag_[i:i+2]) for i in range(len(bag_)) if i%4==1 and i >=2  ]
    stack.append([tuple(bag_[:2])])
    
seen = set()
while len(stack)!=0:
    element = stack.pop()
    if element[-1] == tuple(["shiny", "gold"]) and len(element)>1:
        seen.add(element[0])
    for child in graph[element[-1]]:
        new_element = element.copy()
        new_element.append(child)
        stack.append(new_element)
print(len(seen))
