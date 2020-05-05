class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        
        amounts = [10**6 for i in range(amount+1)]
                
        amounts[0]  = 0
        for coin in coins:
            for amount_ in range(coin,amount+1):
                if amount_ - coin>=0:
                    amounts[amount_] = min(amounts[amount_],amounts[amount_ - coin]+1)
               
        if amounts[amount]==10**6:
            return -1
        return(amounts[amount])
