class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        to_buy = prices[0]
        total = 0
        direction = 0
        for i in range(1,len(prices)):
            if direction==0:
                if prices[i]<=to_buy:
                    to_buy = prices[i]
                else:
                    direction = 1
                    to_sell = prices[i]
            if direction == 1:
                if prices[i]>=to_sell:
                    to_sell = prices[i]
                else:
                    total+=(to_sell - to_buy)
                    direction = 0
                    to_buy = prices[i]
                    
        if direction == 1:
            total+=(to_sell - to_buy)
                    
        return total
                    
        
