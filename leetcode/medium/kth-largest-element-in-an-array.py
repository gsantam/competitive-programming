class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        min_ = min(nums)
        min_ = min(0,min_)
        nums_ = [0 for i in range(max_-min_+1)]
        for num in nums:
            nums_[num-min_] += 1
        i = len(nums_)-1
        while k>0:
            if nums_[i]>0:
                nums_[i]-=1
                k-=1
            else:
                i-=1
        return i+min_
