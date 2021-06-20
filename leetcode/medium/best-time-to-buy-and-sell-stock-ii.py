class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        direction = "descend"
        profit = 0
        buy = None
        for i, price in enumerate(prices):
            if i>=1:
                if direction == "descend":
                    if price>prices[i-1]:
                        direction = "ascend"
                        buy = prices[i-1]
                else:
                    if price<prices[i-1]:
                        direction = "descend"
                        profit+=(prices[i-1] - buy)
            
        if direction == "ascend":
            profit+=(prices[len(prices)-1] - buy)
        return profit
