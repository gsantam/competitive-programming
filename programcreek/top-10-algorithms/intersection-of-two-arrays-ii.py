from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter_1 = Counter(nums1)
        counter_2 = Counter(nums2)
        
        intersection = []
        for element in counter_1:
            if element in counter_2:
                intersection+=[element]*min(counter_1[element],counter_2[element])
                
        return intersection
