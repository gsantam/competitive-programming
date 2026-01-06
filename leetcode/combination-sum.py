from typing import List


class Solution:
    def recurs(self,comb,current_sum,current_element_idx):
        new_comb = tuple([element+1 if i == current_element_idx else 
element for i,element in enumerate(comb)])
        current_sum += self.candidates[current_element_idx]
        if new_comb in self.seen_combs:
            return
        self.seen_combs.add(new_comb)
        if current_sum==self.target:
            match = []
            for i,element in enumerate(self.candidates):
                for rep in range(new_comb[i]):
                    match.append(element)
            self.matches.append(match) 
            return
        if current_sum>self.target:
            return
        for i in range(len(self.candidates)):
            self.recurs(new_comb,current_sum,i)

    def combinationSum(self, candidates: List[int], target: int) -> 
List[List[int]]:
        comb = tuple([0 for i in range(len(candidates))])
        self.matches = []
        self.seen_combs = set()
        self.target = target
        self.candidates = candidates
        for i in range(len(self.candidates)):
            self.recurs(comb,0,i)
        return self.matches

