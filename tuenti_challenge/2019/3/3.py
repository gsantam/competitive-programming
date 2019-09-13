import math
inputs = open("submitInput.txt").read().split("\n")
n = int(inputs[0])
outputs = open("submitOutput.txt","w+")
outputs.truncate()
first = True

j = 1
for i in range(n):
    W, H, F, P= [int(x) for x in inputs[j].split(" ")]
    folds = []
    for f in range(1,F+1):
        folds.append(inputs[f+j])
        
    j +=F
    punches = []
    
    for p in range(1,P+1):
        punches.append([int(x) for x in inputs[p+j].split(" ")])
        
    j+=P+1
    
    prev_punches = tuple(punches)
    w = W
    h = H
    for fold in folds:
        actual_punches = []

        for punche in prev_punches:
            
            if fold == "T":
                actual_punches.append([punche[0],h+punche[1]])
                actual_punches.append([punche[0],h-punche[1]-1])
            if fold == "B":
                actual_punches.append([punche[0],punche[1]])
                actual_punches.append([punche[0],2*h-punche[1] -1 ])
            if fold == "L":
                actual_punches.append([w+ punche[0],punche[1]])
                actual_punches.append([w - punche[0] - 1,punche[1]])
            if fold == "R":
                actual_punches.append([punche[0],punche[1]])
                actual_punches.append([2*w-punche[0]-1,punche[1]])
        prev_punches = tuple(actual_punches)
                
        if fold == "T" or fold == "B":
            h = 2*h
        else:
            w = 2*w
            
        actual_punches = sorted(actual_punches, key = lambda x: (x[0], x[1]))            


    outputs.write("Case #"+str(i+1)+":\n")
    for actual_punche in actual_punches:
        outputs.write(str(actual_punche[0])+" " + str(actual_punche[1]) + "\n")
        

    
outputs.close()
