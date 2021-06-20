bags = open("input.txt").readlines()
stack = []
graph = {}
for bag in bags:    
    bag = bag.replace(" contain no other bags.","").strip()
    bag_ = bag.split(" ")
    graph[tuple(bag_[:2])] = {tuple(bag_[i+1:i+3]):int(bag_[i]) for i in range(len(bag_)) if i%4==0 and i>=1}

def rec(element,mult):
    total = 1
    for child in graph[element].keys():
        total+=rec(child,graph[element][child])
    return total*mult
print(rec(tuple(["shiny", "gold"]),1) - 1)
