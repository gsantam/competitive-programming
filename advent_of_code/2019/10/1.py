import math
grid = open("input.txt","r").read().strip().split("\n")
asteroids_positions = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y]=="#":
            asteroids_positions.append((y,x))

all_unique_asteroids = {}
for x in asteroids_positions:
    unique_asteroids = set()
    for y in asteroids_positions:
        if x!=y:
            unitary_vector = (y[0] - x[0],y[1] - x[1])
            norm = math.sqrt(unitary_vector[0]**2 + unitary_vector[1]**2)
            unitary_vector = tuple([float('%.3f'%(x/norm)) for x in unitary_vector])
            unique_asteroids.add(unitary_vector)
    all_unique_asteroids[x] = len(unique_asteroids)
    
print(max(all_unique_asteroids.values()))
print([x for x in all_unique_asteroids if all_unique_asteroids[x]==max(all_unique_asteroids.values())])
