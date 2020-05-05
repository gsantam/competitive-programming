import operator as op
from functools import reduce




class Solution:
    
    def threeSumMulti(self, A,target) -> int:
        dict_values = dict()
        for i,val in enumerate(A):
            if val not in dict_values:
                dict_values[val] = 0
            dict_values[val]+=1
            
        n_ways = 0
        combs = set()
        for i in dict_values:
            for j in dict_values:
                k = 
                if i<j and target - i -j in dict_values:
                    k = target - i -j
                    combs.add(tuple(sorted((i,j,k))))
        for comb in combs:
            to_add = 0
            comb_same = set(comb)
            if len(comb_same)==3:
                to_add = dict_values[comb[0]]*dict_values[comb[1]]*dict_values[comb[2]]
            elif len(comb_same)==1:
                if dict_values[comb[0]]>=3:
                    to_add = dict_values[comb[0]]*(dict_values[comb[0]]-1)*(dict_values[comb[0]]-2)/6
                else:
                    to_add = 0
            else:
                if comb[0]==comb[1]:
                    same_value = 0
                    other = 2
                elif comb[0]==comb[2]:
                    same_value = 0
                    other = 1
                else:
                    same_value = 1
                    other = 0
                if dict_values[comb[same_value]]>=2:   
                    to_add = dict_values[comb[same_value]]*(dict_values[comb[same_value]]-1)/2
                    to_add*=dict_values[comb[other]]
                else:
                    to_add=0
                
            n_ways = ((n_ways+to_add)%(10**9 + 7))
                            
        return int(n_ways)


            
                
            
        
