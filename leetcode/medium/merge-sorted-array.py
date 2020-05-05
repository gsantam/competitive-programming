"""
[4,5,6,0,0,0]
[1,2,3]

[1,5,6,4,0,0]
[1,2,3,4,5,0]

"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        while i>=0 or j>=0:
            if i>=0:
                ele1 = nums1[i]
            else:
                ele1 = -10**6
            if j>=0:
                ele2 = nums2[j]
            else:
                ele2 = -10**6  
                
            if ele1>=ele2:
                nums1[i+j+1] = ele1
                i-=1
            else:
                nums1[i+j+1] = ele2
                j-=1

        """
        Do not return anything, modify nums1 in-place instead.
        """
        
                
