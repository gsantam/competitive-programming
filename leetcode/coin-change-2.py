class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        if amount == 0:
            return 1
        if len(coins)==0:
            if amount == 0:
                return 1
            else:
                return 0
            
        
        coins = [coin for coin in coins if coin<=amount]
        coins = sorted(coins)

                
        n_ways_by_amount = [[0 for i in range(len(coins))] for j in range(amount+1)]   
        
        for i in range(len(coins)):
            n_ways_by_amount[0][i] = 1
        total_sum = 0
            
        for current_amount in range(1,amount+1):
            cum = 0
            for j in range(len(coins)):
                if current_amount - coins[j]>=0:
                    n_ways_by_amount[current_amount][j] += n_ways_by_amount[current_amount - coins[j]][j]
                cum+=n_ways_by_amount[current_amount][j]
                n_ways_by_amount[current_amount][j] = cum
            
                
        return n_ways_by_amount[current_amount][len(coins)-1]
