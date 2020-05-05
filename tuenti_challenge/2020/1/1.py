input_ = open("submitInput.txt","r")
output = []
order = {"S":0,"P":1,"R":2}
for i,line in enumerate(input_.readlines()[1:]):
    p1,p2 = line.strip().split(" ")
    if p1==p2:
        out = "-"
    else:
        if (order[p1]+1)%3==order[p2]:
            out = p1
        else:
            out = p2
    output.append(out)
    
output_file = open("submitOutput.txt","w+")
output_file.write("\n".join(["Case #"+str(i+1)+": "+str(x) for i,x in enumerate(output)]))
output_file.close()
