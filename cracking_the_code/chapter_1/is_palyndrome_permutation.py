from collections import Counter
def is_palyndrome_permutation(string):
    counter =Counter()
    for char in string:
        counter[char]+=1
        
    find_odd = False
        
    for word in counter:
        if counter[word] %2 == 1:
            if find_odd:
                return False
            find_odd = True
    return True
        
    
