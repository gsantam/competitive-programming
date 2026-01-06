class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = [num-1 for num in nums]
        for i in range(len(nums)):
            while nums[i]!=i and nums[i]!=-1:
                swp = nums[nums[i]]
                if swp==-1:
                    break
                elif swp==nums[i]:
                    nums[nums[i]] = -1
                    break
                else:
                    nums[nums[i]] = nums[i]
                    nums[i] = swp
        return [i+1 for i in range(len(nums)) if nums[i]==-1]
