orbits = open("input.txt","r").read().split("\n")
orbit_dict = dict()
in_orbit = set()
for orbit in orbits:
    if orbit!='':
        planet_1 = orbit.split(")")[0]
        planet_2 = orbit.split(")")[1]
        if planet_1 not in orbit_dict:
            orbit_dict[planet_1] = []
        if planet_2 not in orbit_dict:
            orbit_dict[planet_2] = []
        orbit_dict[planet_1].append(planet_2)
        orbit_dict[planet_2].append(planet_1)
    
found = False
stack = [(0,"YOU")]
visited = set()
while not found:
    planet_ = stack.pop()
    planet = planet_[1]
    depth  = planet_[0]
    if planet not in visited:
        visited.add(planet)
        if planet=="SAN":
            found = True
        else:
            if planet in orbit_dict:
                for orbit_planet in orbit_dict[planet]:
                    stack.append((depth+1,orbit_planet))
print(depth -2 )
