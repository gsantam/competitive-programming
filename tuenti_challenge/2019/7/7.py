import math
def notSoComplexHash(inputText):
    my_hash = [0 for x in range(16)]
    textBytes = inputText.encode("ISO_8859_1")
    for i,byte in enumerate(textBytes):
        my_hash[i%16] = (my_hash[i%16] + textBytes[i])
    my_hash = [x%256 for x in my_hash]
    return [(256-x) * (-1) if x >  127  else x for x in my_hash]

def get_number(x):
    return (256-x) * (-1) if x >  127  else x 

def get_diff(original,generated):
    if original>=generated:
        diff  = original - generated
    else:
        diff = (128-generated) +original + 128
    
    if diff < 48:
        diff = 256 + abs(original - generated)
    return diff
    
    

max_char_code = 122

import math
inputs = open("submitInput.txt").read().split("\n")
m = int(inputs[0])
outputs = open("submitOutput.txt","w+")
outputs.truncate()
first = True

j = 1
for i in range(m):
    print(i)
    N = int(inputs[j])
    text_original = ""
    
    for k in range(N):
        text_original+=inputs[j+k+1]
    
    j+=N+1
    N = int(inputs[j])
    
    text_modified = ""
    for k in range(N):
        text_modified+=inputs[j+k+1]  
    
    j+=N+1
    
    text_original = text_original.replace("\n","")
    text_original = text_original.replace("\r","")

    hash_original = notSoComplexHash(text_original)
    
    text_modified = text_modified.replace("\n","")
    text_modified = text_modified.replace("\r","")

    text_starts = text_modified.find("---")+ len("---")
    
    is_the_same = False
    n = 1
    while not is_the_same or bad:
        bad = False
        new_text_modified = text_modified[:text_starts]+"".join(["\0" for x in range(n)])+text_modified[text_starts:]
        text_to_insert = ""

        for k in range(n):
            #print(len(new_text_modified))
            generated_hash = notSoComplexHash(new_text_modified)
            position = (text_starts + k)%16
            diff = get_diff(hash_original[position],generated_hash[position])
            number_of_repetitions = 1+ (n-k-1)//16
            my_position = k//16
            multiplier = 0
            while number_of_repetitions*48 > diff + 256*multiplier:
                multiplier+=1
            diff = diff + 256*multiplier
            n_122 = (diff-48)//122
            rest = diff - 122*n_122

            if number_of_repetitions>n_122+1:
                text_to_insert+="0"
            else:
                if not(rest >= 48 and rest<=122):
                    bad = True
                text_to_insert+=str(chr(rest))

            new_text_modified = text_modified[:text_starts]+text_to_insert+"".join(["\0" for x in range(n-k-1)])+text_modified[text_starts:]           

        n+=1
        generated_hash = notSoComplexHash(new_text_modified)
        if generated_hash == hash_original and bad == False:
            is_the_same = True
            
    if first:
        first = False
    else:
        outputs.write("\n")
    outputs.write("Case #"+str(i+1)+": "+text_to_insert)
    
outputs.close()
