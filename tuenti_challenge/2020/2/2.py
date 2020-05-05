input_ = open("submitInput.txt","r")
output = []
lines = input_.readlines()[1:]
i = 0
while i<len(lines):
    line = lines[i].strip()
    i+=1
    players = set()
    looser_players = set()
    n_matches = int(line)
    for j in range(n_matches):
        line = lines[i]
        p1,p2,result = line.split(" ")
        players.add(p1)
        players.add(p2)
        if int(result) == 1:
            looser_players.add(p2)
        else:
            looser_players.add(p1)
        i+=1
    output.append(list(players - looser_players)[0])
    
output_file = open("submitOutput.txt","w+")
output_file.write("\n".join(["Case #"+str(i+1)+": "+str(x) for i,x in enumerate(output)]))
output_file.close()
