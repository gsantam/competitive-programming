class Solution:
    def helper(self,seq,taken,nums):
        if len(seq) == len(nums):
            return [seq]
        seqs = []
        for i in range(len(taken)):
            if taken[i]==0:
                taken_ = taken.copy()
                seq_ = seq.copy()
                seq_.append(nums[i])
                taken_[i] = 1
                seqs+=self.helper(seq_,taken_,nums)
        return seqs
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        return self.helper([],[0 for i in range(len(nums))],nums)
        
        
