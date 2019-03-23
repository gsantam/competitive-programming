t = int(input())
import string
abecedary = list(string.ascii_uppercase)
for i in range(t):
    n= int(input())
    parties_ = [int(x) for x in input().split(" ")]
    parties = dict()
    for j in range(len(parties_)):
        parties[abecedary[j]] = parties_[j]

    sequence = ""
    while len(parties)!=0:            
        max_members = 0
        if len(parties) == 2:
            sequence+=" "+list(parties.keys())[0]+list(parties.keys())[1]
            parties[list(parties.keys())[0]]-=1
            parties[list(parties.keys())[1]]-=1
        else:
            for party in parties:
                if parties[party]>max_members:
                    max_members = parties[party]
                    max_party = party
            sequence+=" "+max_party
            parties[max_party]-=1
        parties = {party:parties[party] for party in parties if parties[party]!=0}
    print("Case #"+str(i+1)+":"+sequence)
            
        
    
    
