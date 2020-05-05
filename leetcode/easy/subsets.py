class Solution:
    def helper(self,length,current_seq,i,nums):
        if length == len(current_seq):
            self.subsets_coll.append(current_seq)
            return
        
        for j in range(i+1,len(nums)):
            if length - len(nums) <= len(nums) - j: 
                self.helper(length,current_seq+[nums[j]],j,nums)
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets_coll = []
        for i in range(len(nums)+1):
            self.helper(i,[],-1,nums)
            
        return self.subsets_coll
        
