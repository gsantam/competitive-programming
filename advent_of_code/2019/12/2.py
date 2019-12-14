initial_configs = open("input.txt","r").read().strip().split("\n")
moons = []
for initial_config in initial_configs:
    initial_config =initial_config.strip(">").split(",")
    moons.append([[int(initial_config[0][3:]),int(initial_config[1][3:]),int(initial_config[2][3:])],[0,0,0]])
    
first_component_repetition = []
for component in range(3):
    states = set()
    repeated = False
    timestamp = 0
    while not repeated:
        actual_state = tuple(tuple(tuple(y for i,y in enumerate(config) if i==component ) for config in x) for x in moons)
        if actual_state in states:
            first_component_repetition.append(timestamp)
            repeated= True
        states.add(actual_state)
        for moon1 in moons:
            for moon2 in moons:
                if moon1!=moon2:
                    for i in range(3):
                        if moon1[0][i] > moon2[0][i]:
                            moon1[1][i]-=1
                        if moon1[0][i] < moon2[0][i]:
                            moon1[1][i]+=1
        for moon in moons:
            for i in range(3):
                moon[0][i]+=moon[1][i]
        timestamp+=1
        
import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

first_second_repetition = lcm(first_component_repetition[0],first_component_repetition[1])
first_repetition = lcm(first_second_repetition,first_component_repetition[2])
print(first_repetition)


