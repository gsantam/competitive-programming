class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        if K == len(A):
            return sum(A) 
        if K == 1:
            return sum(A)/len(A)
        
        dynamic_Ks = [[0 for j in range(len(A))] for i in range(K+1)]
        
        for i in range(1,K+1):
            for j in range(len(A)):
                if i == 1:
                    dynamic_Ks[i][j] = sum(A[0:j+1])  / (j+1)
                else:
                    if i >= (j+1):
                        dynamic_Ks[i][j] = sum(A[0:j+1])
                    else:
                        max_average_sum = 0
                        for k in range(j):
                            right_array = A[k+1:j+1]
                            max_average_sum = max(max_average_sum,dynamic_Ks[i-1][k] + sum(right_array)/len(right_array))
                            
                        dynamic_Ks[i][j] = max_average_sum
                        
        return dynamic_Ks[K][len(A)-1]
                            
        
        
"""
class Solution:
    def helper(self,pos,k):
        if (pos,k) in self.memo:
            return self.memo[(pos,k)]
        cur_list = self.list[0:pos+1]
        if k==1:
            self.memo[(pos,k)] = sum(cur_list) / len(cur_list)
            return sum(cur_list) / len(cur_list)
        if k>=pos+1:
            self.memo[(pos,k)] = sum(cur_list)
            return sum(cur_list)
        max_value = 0
        for i in range(pos):
            end_list = cur_list[i+1:]
            if len(end_list)>=1:
                max_value = max(max_value,self.helper(i,k-1) + sum(end_list)/len(end_list))
            
        self.memo[(pos,k)] = max_value
        return max_value
            
    
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        self.memo = dict()
        self.list = A
        return self.helper(len(A),K)
                            
        
"""
