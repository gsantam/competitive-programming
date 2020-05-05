def determine_best_total(total):
    
    def determine_number(initial_height,my_total,x=1,y=1):
        total_ = initial_height*x*y
        current_height = initial_height
        i = 2
        while current_height!=2:
            current_height -= 2
            total_+=current_height*(2*x+2*y+4*((i-1)*2-1))
            i+=1
            current_height+=1
            total_+=current_height*(2*x+2*y+4*((i-1)*2-1))
            i+=1
            if total_>my_total:
                return 2**62
        return total_

    left = 1
    right = min(1000000,total)

    while right-left>=2:
        middle = (left+right)//2
        n_middle = determine_number(middle,total)
        if n_middle>total:
            right = middle -1
        else:
            left = middle
    if right <3:
        return "IMPOSSIBLE"
    if determine_number(right,total)<=total:
        best_height = right
    else:
        best_height = left
    if best_height <3:
        return "IMPOSSIBLE"
    
    x = 1
    y = 1
    current_total = 0
    while current_total<=total:
        best_total = current_total
        current_total = determine_number(best_height,total,x,y)

        if x==y:
            x+=1
        else:
            y+=1
    return str(best_height)+ " " + str(best_total)



input_ = open("submitInput.txt","r")
output = []
for line in input_.readlines()[1:]:
    print(line)
    line = line.strip().split(" ")
    n = int(line[0])
    my_output = determine_best_total(n)
    output.append(my_output)
    
output_file = open("submitOutput.txt","w+")
output_file.write("\n".join(["Case #"+str(i+1)+": "+str(x) for i,x in enumerate(output)]))
output_file.close()
