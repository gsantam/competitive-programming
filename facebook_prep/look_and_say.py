def look_and_say(n):
    assert type(n) == int
    assert n>=1
    prev_sequence = "1"
    for i in range(n):
        print(prev_sequence)
        sequence = ""
        rep_char = 0
        for i,char in enumerate(prev_sequence):
            if i==0 or prev_sequence[i-1]==char:
                rep_char+=1
            else:
                sequence+=str(rep_char)+prev_sequence[i-1]
                rep_char = 1
        
        sequence+=str(rep_char)+char
        prev_sequence = sequence
        
look_and_say(-1)
