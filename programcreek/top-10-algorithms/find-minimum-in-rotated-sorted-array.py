class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        min_so_far = 10**6
        while True:
            mid = (left + right)//2
            if right-left<=2:
                return min(nums[left],min(nums[right],nums[(left+right)//2]))
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[left]:
                right = mid
            else:
                right = mid
        return min_so_far
