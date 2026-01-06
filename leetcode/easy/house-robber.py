class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        money_incl = [0 for i in range(len(nums))]
        money_excl = [0 for i in range(len(nums))]
        money_incl[0] = nums[0]
        money_incl[1] = nums[1]
        money_excl[1] = nums[0]
        max_money = 0
        for house in range(len(nums)):
            if house>=2:
                money_incl[house] = 
max(money_incl[house-2],money_excl[house-1]) + nums[house]
                money_excl[house] = 
max(money_incl[house-1],money_excl[house-1])
            max_money = max(max_money,money_excl[house])
            max_money = max(max_money,money_incl[house])
        return max_money
