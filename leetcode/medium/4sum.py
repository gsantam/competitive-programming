from typing import List
from collections import defaultdict

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        counts = defaultdict(lambda: 0)
        nums_2 = []
        for num in nums:
            if counts[num]<=4:
                nums_2.append(num)
            counts[num]+=1
        sums = defaultdict(lambda: [])
        for i in range(len(nums_2)):
            for j in range(i+1,len(nums_2)):
                sums[nums_2[i]+nums_2[j]].append([i,j])
        quad_sums = set([])
        for sum_ in sums:
            for pair_1 in sums[sum_]:
                if target-sum_ in sums:
                    for pair_2 in sums[target-sum_]:
                        indices = set([pair_1[0],pair_1[1],pair_2[0],pair_2[1]])
                        if len(indices)==4:
                            
quad_sums.add(tuple(sorted([nums_2[pair_1[0]],nums_2[pair_1[1]],nums_2[pair_2[0]],nums_2[pair_2[1]]])))
        return quad_sums
