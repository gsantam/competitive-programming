import math
inputs = open("submitInput.txt").read().split("\n")
n = int(inputs[0])
outputs = open("submitOutput.txt","w+")
outputs.truncate()
first = True

def lcm(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm
j = 1
for i in range(n):
    N = int(inputs[j])
    
    numbers ={}
    for number in [int(x) for x in inputs[j+1].split(" ")]:
        if number not in numbers:
            numbers[number] = 0
        numbers[number]+=1
        
    repetition= dict()
    for number in numbers:
        lcm_number = lcm([number, numbers[number]])
        repetition[number] = lcm_number//numbers[number]
        #lcms[number] = lcm([number, numbers[number]])
        
        
    final_lcm = lcm(list(repetition.values()))
    den = 0
    nom = 0
    for number in repetition:
        den += final_lcm*numbers[number]//number
        nom += (final_lcm*numbers[number]*number)//number
        
    my_gcd = math.gcd(den, nom)

        
    j+=2
    if first:
        first = False
    else:
        outputs.write("\n")
    outputs.write("Case #"+str(i+1)+": "+str(nom//my_gcd)+"/"+str(den//my_gcd))

    
outputs.close()
