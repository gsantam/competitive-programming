import math
inputs = open("submitInput.txt").read().split("\n")
n = int(inputs[0])
outputs = open("submitOutput.txt","w+")
outputs.truncate()
first = True

j = 1

keyboard = [["1","2","3","4","5","6","7","8","9","0"],
            ["Q","W","E","R","T","Y","U","I","O","P"],
            ["A","S","D","F","G","H","J","K","L",";"],
            ["Z","X","C","V","B","N","M",",",".","-"]]

keyboard_dict = {keyboard[x][y]:(x,y) for x in range(len(keyboard)) for y in range(len(keyboard[0]))}
keyboard_dict_inv = {(x,y):keyboard[x][y] for x in range(len(keyboard)) for y in range(len(keyboard[0]))}


for i in range(n):
    who = inputs[j]
    message = inputs[j+1]
    movement_x = keyboard_dict[message[-1]][0] - keyboard_dict[who][0]
    movement_y =keyboard_dict[message[-1]][1] - keyboard_dict[who][1]
    translated_message = "".join([keyboard_dict_inv[((keyboard_dict[char][0]-movement_x)%len(keyboard),(keyboard_dict[char][1]-movement_y)%len(keyboard[0]))] if char!=" " else " " for char in message])
    #print(message)
    
    j+=2
    
    if first:
        first = False
    else:
        outputs.write("\n")
    outputs.write("Case #"+str(i+1)+": "+translated_message)
outputs.close()
