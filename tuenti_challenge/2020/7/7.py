qwerty = "qwertyuiopasdfghjklzxcvbnm,. "
dvorak = "',.pyfgcrlaoeuidhtn;qjkxbmwv "

DVORAK = {char:i for i,char in enumerate(DVORAK)}

input_ = open("testInput.txt","r")
output = []
for line in input_.readlines()[1:]:
    new_line = ""
    for char in line[:-1]:
        new_line+=QWERTY[DVORAK[char]]
    output.append(new_line)
    
output_file = open("submitOutput.txt","w+")
output_file.write("\n".join(["Case #"+str(i+1)+": "+str(x) for i,x in enumerate(output)]))
output_file.close()
