import math
inputs = open("submitInput.txt").read().split("\n")
n = int(inputs[0])
outputs = open("submitOutput.txt","w+")
outputs.truncate()
first = True
for i,case in enumerate(inputs[1:-1]):
    n, m = [int(x) for x in case.split(" ")]
    total_tortillas = math.ceil(n/2) + math.ceil(m/2)
    if first:
        first = False
    else:
        outputs.write("\n")
    outputs.write("Case #"+str(i+1)+": "+str(total_tortillas))

    
outputs.close()
