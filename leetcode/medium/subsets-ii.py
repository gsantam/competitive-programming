from collections import Counter
from typing import List

class Solution:

    def recursion(self,current,pos):
        if pos==len(self.count_keys):
            self.all_sets.append(current)
            return

        for n in range(self.count_values[pos]+1):
            new_current = current.copy()
            new_current+=[self.count_keys[pos]]*n
            self.recursion(new_current,pos+1)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        count_dict = Counter(nums)
        self.count_keys = list(count_dict.keys())
        self.count_values = list(count_dict.values())
        self.all_sets = []
        self.nums = nums
        self.recursion([],0)
        return self.all_sets
