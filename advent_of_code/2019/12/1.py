initial_configs = open("input.txt","r").read().strip().split("\n")
moons = []
for initial_config in initial_configs:
    initial_config =initial_config.strip(">").split(",")
    moons.append([[int(initial_config[0][3:]),int(initial_config[1][3:]),int(initial_config[2][3:])],[0,0,0]])
    
timestamps = 1000
for i in range(timestamps):
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
            
sum_absolute = [[sum([abs(x) for x in prop]) for prop in moon] for moon in moons]
print(sum([moon[0]*moon[1] for moon in sum_absolute]))
