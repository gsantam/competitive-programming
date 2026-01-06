class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        combs = [0 for i in range(target+1)]
        combs[0] = 1
        for i in range(len(combs)):
            for num in nums:
                if i - num >= 0:
                    combs[i] += combs[i - num]
        return combs[target]
