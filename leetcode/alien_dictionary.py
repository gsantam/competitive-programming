words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

smaller_than_me = dict()

for i in range(1,len(words)):
    word_1 = words[i-1]
    word_2 = words[i]

    for j in range(min(len(word_1),len(word_2))):
        
        if word_1[j] not in smaller_than_me:
            smaller_than_me[word_1[j]] = set()
        if word_2[j] not in smaller_than_me:
            smaller_than_me[word_2[j]] = set()  
            
        if word_1[j]!=word_2[j]:
            smaller_than_me[word_2[j]].add(word_1[j])  
            break
            
letters_in_order = []

while len(smaller_than_me)>0:
    smaller_letter = None
    for letter in smaller_than_me:
        if len(smaller_than_me[letter])==0:
            if smaller_letter is None:
                smaller_letter = letter
            else:
                print("error")
    letters_in_order.append(smaller_letter)
    if smaller_letter is None:
        print("error")
        break
    del smaller_than_me[smaller_letter]
    for letter in smaller_than_me:
        if smaller_letter in smaller_than_me[letter]:
            smaller_than_me[letter].remove(smaller_letter)
            
print(letters_in_order)
        
