from collections import Counter

class Solution:
    def helper(self,seq,current_counts,nums,count,n):
        if len(seq) == n:
            return [seq]
        seqs = []
        for i in range(len(nums)):
            if current_counts[nums[i]]<count[nums[i]]:
                current_counts_= current_counts.copy()
                current_counts_[nums[i]]+=1
                seq_ = seq.copy()
                seq_.append(nums[i])
                seqs+=self.helper(seq_,current_counts_,nums,count,n)
        return seqs
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        count = Counter(nums)
        nums = list(count.keys())
        current_counts = {num:0 for num in nums}
        
        if len(nums)==0:
            return []
        return self.helper([],current_counts,nums,count,n)
        
        
