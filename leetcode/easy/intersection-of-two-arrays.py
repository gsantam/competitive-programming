from collections import Counter

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        total_int = []
        
        for element_1 in c1:
            if element_1 in c2:
                total_int+=[element_1]
        return total_int
            
        
        
