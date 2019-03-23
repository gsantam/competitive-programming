t = int(input())
import string
for i in range(t):
    d, n = [int(x) for x in input().split(" ")]
    horses = []
    maximimum_speed = 10000000000000000.
    for j in range(n):
        horse = [int(x) for x in input().split(" ")]
        time_to_destination = (d - horse[0])/horse[1]
        my_speed = d / time_to_destination
        maximimum_speed = min(maximimum_speed,my_speed)
    print("Case #"+str(i+1)+": "+"%.8f" % maximimum_speed)
