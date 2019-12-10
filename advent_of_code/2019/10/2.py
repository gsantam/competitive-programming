place = (28,29)
import math
grid = open("input.txt","r").read().strip().split("\n")
grid_ = [[0 for j in range(len(grid[0]))] for i in range(len(grid[0]))]

asteroids_positions = []
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y]=="#":
            asteroids_positions.append((y,x))
            
asteroids_positions_angle_distance = {}
for x in asteroids_positions:
    if x!=place:
        vector = (x[0] - place[0],x[1] - place[1])
        norm = math.sqrt(vector[0]**2 + vector[1]**2)
        angle = math.acos(( place[1]-x[1])/ norm)
        if (x[0] - place[0])>=0:
            asteroids_positions_angle_distance[x] = (float('%.3f'%angle),float('%.3f'%norm))
        else:
            asteroids_positions_angle_distance[x] = (float('%.3f'%(2*math.pi-angle)),float('%.3f'%norm))

            
import pandas as pd
asteroids_positions_angle_distance = pd.DataFrame.from_dict(asteroids_positions_angle_distance,orient = "index").rename(columns = {0:"angle",1:"distance"}).sort_values(["angle","distance"]).drop_duplicates("angle",keep="first")
asteroids_positions_angle_distance["index"] = list(range(1,len(asteroids_positions_angle_distance)+1))
index= asteroids_positions_angle_distance[asteroids_positions_angle_distance["index"]==200].index

print(index[0][0]*100 + index[0][1])
