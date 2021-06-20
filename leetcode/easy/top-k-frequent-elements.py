import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting = dict()
        for num in nums:
            if num not in counting:
                counting[num] = 0
            counting[num]+=1
        h = []
        for element in counting:
            heapq.heappush(h,[-counting[element],element])
        
        top_k = []
        for i in range(k):
            top_k.append(heapq.heappop(h)[1])
        return top_k
        
