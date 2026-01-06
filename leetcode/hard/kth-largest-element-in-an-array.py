class Solution:
    def reorderpivot(self,nums):
        i = 0
        j = len(nums)-2
        pivot = nums[len(nums)-1]
        while i<j:
            if nums[i]<=pivot:
                i+=1
            elif nums[j]>pivot:
                j-=1
            else:
                swp = nums[i]
                nums[i] = nums[j]
                nums[j] = swp
        if pivot<nums[j]:
            nums[len(nums)-1] = nums[j]
            nums[j] = pivot
            return nums[:j],nums[j:]
        return nums[:len(nums)-1],nums[len(nums)-1:]
        

    def findKthLargest(self, nums: List[int], k: int) -> int:
        left,right = self.reorderpivot(nums)
        while len(right)!=k:
            if len(right)<k:
                k = k-len(right)
                left,right = self.reorderpivot(left)
            else:
                left,right = self.reorderpivot(right)
        return right[0]
