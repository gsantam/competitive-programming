class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        bef = []
        exact = []
        after = []
        for num in nums:
            if num<pivot:
                bef.append(num)
            elif num==pivot:
                exact.append(num)
            else:
                after.append(num)
        return bef + exact + after
            
