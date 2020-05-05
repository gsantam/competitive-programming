class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        current_unhappy_costumers_in_range = 0
        customers_happy = 0
        max_customers_unhappy = 0
        for i,customer in enumerate(customers):
            if grumpy[i]==1:
                current_unhappy_costumers_in_range+=customers[i]
            else:
                customers_happy+=customers[i]
            if i>=X:
                if grumpy[i-X]==1:
                    current_unhappy_costumers_in_range-=customers[i-X]
                    
            max_customers_unhappy = max(max_customers_unhappy,current_unhappy_costumers_in_range)
              
        return customers_happy + max_customers_unhappy
        
            
        
