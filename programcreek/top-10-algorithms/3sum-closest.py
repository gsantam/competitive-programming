class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest_diff = 10**10
        for i,num in enumerate(nums):
            j = 0
            k = len(nums)-1
            while j<k:
                if j==i or k==i:
                    if j==i:
                        j+=1
                    else:
                        k-=1
                else:
                    current_sum = nums[i] + nums[j] + nums[k]
                    if abs(current_sum-target)<closest_diff:
                        closest_diff = abs(current_sum-target)
                        closest_sum = current_sum
                    if current_sum<=target:
                        j+=1
                    else:
                        k-=1
        return closest_sum
                    
                
        
