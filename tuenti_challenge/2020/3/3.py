import re
from collections import Counter
accepted_letters = set([chr(i) for i in range(ord('a'),ord('z')+1)])
accepted_letters = accepted_letters.union(set(['á','é','í','ó','ú','ñ','ü'," ","\n"]))
text = open("pg17013.txt","r").read().lower()
cleaned_text= ""
for char in text:
    if char in accepted_letters:
        cleaned_text+=char
    else:
        cleaned_text+=" "

cleaned_text = re.sub('\n', ' ', cleaned_text)
cleaned_text = re.sub(' +', ' ', cleaned_text)
cleaned_text
counter = Counter([x for x in cleaned_text.split(" ") if len(x)>=3])
counter = sorted({(-counter[word],word)for word in counter})
inv_indx = {word_pair[1]: (i,word_pair[0]) for i, word_pair in enumerate(counter)}

input_ = open("submitInput.txt","r")
output = []
for line in input_.readlines()[1:]:
    line = line.strip()
    try:
        pos = int(line)
        count = counter[pos-1]
        output.append(count[1]+ " " + str(-count[0]))
    except Exception as e:
        idx = inv_indx[line]
        output.append(str(-idx[1])+ " #" + str(idx[0]+1))
        
output_file = open("submitOutput.txt","w+")
output_file.write("\n".join(["Case #"+str(i+1)+": "+str(x) for i,x in enumerate(output)]))
output_file.close()
