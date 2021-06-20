seats = open("input.txt","r").readlines()
highest = 0
for seat in seats:
    down = 0
    up = 127
    left = 0
    right = 7
    for letter in seat:
        if letter == "F":
            up = (down+up)//2
        if letter == "B":
            down = (down+up)//2
        if letter == "R":
            left = (left+right)//2
        if letter == "L":
            right = (left+right)//2
    seat_id = up*8 + right
    highest = max(highest,seat_id)
print(highest)
