import math
inputs = open("submitInput.txt").read().split("\n")
n = int(inputs[0])
outputs = open("submitOutput.txt","w+")
outputs.truncate()
first = True

j = 1
for i in range(n):
    n_planets = int(inputs[j])
    number_paths = {}
    for k in range(1,n_planets+1):
        planet_from = inputs[k+j].split(":")[0]
        planets_to = inputs[k+j].split(":")[1].split(",")
        for planet_to in planets_to:
            if planet_to not in number_paths:
                number_paths[planet_to] = 0
            if planet_from == "Galactica":
                number_paths[planet_to] = 1
            else:
                number_paths[planet_to] += number_paths[planet_from]
                
    j +=n_planets+1
    
    if first:
        first = False
    else:
        outputs.write("\n")
    outputs.write("Case #"+str(i+1)+": "+str(number_paths["New Earth"]))

    
outputs.close()

