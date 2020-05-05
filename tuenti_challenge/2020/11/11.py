def n_ways(n,restricted_numbers): 
  
    table =[0] * (n+1 ) 
    table[0] = 1
    for i in range(1, n ): 
        for j in range(i , n + 1): 
            if i not in restricted_numbers:
                table[j] +=  table[j - i]   
    return table[n] 


input_ = open("submitInput.txt","r")
output = []
for line in input_.readlines()[1:]:
    line = line.strip().split(" ")
    n = int(line[0])
    restricted_numbers = set([int(x) for x in line[1:]])
    output.append(n_ways(n,restricted_numbers))
output_file = open("submitOutput.txt","w+")
output_file.write("\n".join(["Case #"+str(i+1)+": "+str(x) for i,x in enumerate(output)]))
output_file.close()
