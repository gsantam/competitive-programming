
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums)==0:
            if k==0:
                return 1
            return 0
        cumulative = 0
        dict_cumulatives = {0:1}
        totals = 0
        for num in nums:
            cumulative+=num
            if cumulative - k in dict_cumulatives:
                totals+=dict_cumulatives[cumulative- k]
                
            if cumulative not in dict_cumulatives:
                dict_cumulatives[cumulative]=0
            dict_cumulatives[cumulative]+=1
        return totals            
        
