class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums  = [(num,i) for i,num in enumerate(nums)]
        sorted_nums = sorted(nums,reverse = True)
        pos = [0 for i in range(len(nums))]
        for i,element in enumerate(sorted_nums):
            idx = element[1]
            if i == 0:
                rank = "Gold Medal"
            elif i == 1:
                rank = "Silver Medal"
            elif i == 2:
                rank = "Bronze Medal"
            else:
                rank = str(i+1)
                
            pos[idx]  = rank
        return pos
            
        
