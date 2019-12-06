orbits = open("input.txt","r").read().split("\n")
orbit_dict = dict()
in_orbit = set()
for orbit in orbits:
    if orbit!='':
        planet_1 = orbit.split(")")[0]
        planet_2 = orbit.split(")")[1]
        if planet_1 not in orbit_dict:
            orbit_dict[planet_1] = []
        orbit_dict[planet_1].append(planet_2)
        in_orbit.add(planet_2)
        
leafs = [x for x in orbit_dict.keys() if x not in in_orbit]
total = 0
for leaf in leafs:
    stack = []
    stack.append((0,leaf))
    while len(stack)>0:
        planet_ = stack.pop()
        planet = planet_[1]
        depth  = planet_[0]
        total+=depth
        if planet in orbit_dict:
            for orbit_planet in orbit_dict[planet]:
                stack.append((depth+1,orbit_planet))
print(total)
