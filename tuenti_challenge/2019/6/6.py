import math
inputs = open("submitInput.txt").read().split("\n")
n = int(inputs[0])
outputs = open("submitOutput.txt","w+")
outputs.truncate()
first = True

j = 1


for i in range(n):
    if first:
        first = False
    else:
        outputs.write("\n")
        
    n_words = int(inputs[j])
    smaller_than = {}

    words = []
    for k in range(n_words):
        for char in inputs[j+k+1]:
            smaller_than[char] = set()
        
    for k in range(n_words-1):
        
        p = 0
        while p<len(inputs[j+k+1]) and p<len(inputs[j+k+2]) and inputs[j+k+1][p]==inputs[j+k+2][p]:
            p+=1
            
        if not (p==len(inputs[j+k+1]) or p==len(inputs[j+k+2])):
            smaller_than[inputs[j+k+1][p]].add(inputs[j+k+2][p])
            
        
    ambiguous = False
    visited = []
    while not ambiguous and len(visited)<len(smaller_than.keys()):
        visited_letters = []
        for letter in smaller_than:
            if letter not in visited:
                has_bigger_letter = False
                for bigger_letter in smaller_than[letter]:
                    if bigger_letter not in visited:
                        has_bigger_letter = True
                        break
                if not has_bigger_letter:
                    visited_letters.append(letter)

        if len(visited_letters)!=1:
            ambiguous = True
        else:
            visited.append(visited_letters[0])
                
    if ambiguous == True:
        outputs.write("Case #"+str(i+1)+": AMBIGUOUS")
    else:
        outputs.write("Case #"+str(i+1)+": "+" ".join(list(reversed(visited))))

                                
    
    j+=n_words+1
    
outputs.close()
