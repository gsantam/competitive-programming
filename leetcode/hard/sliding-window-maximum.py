class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d_queue = deque()
        current_i = 0
        max_element = nums[0]
        maxes = []
        for i in range(len(nums)):
            if len(d_queue)==0 or nums[i]>=d_queue[-1][0]:
                d_queue.append([nums[i],i])
            else:
                while len(d_queue)!=0 and d_queue[0][0]<=nums[i]:
                    found = True
                    d_queue.popleft()
                d_queue.appendleft([nums[i],i])
            while len(d_queue)!=0 and d_queue[-1][1]<i-k+1:
                d_queue.pop()
            while len(d_queue)!=0 and d_queue[0][1]<i-k+1:
                d_queue.popleft()

            if current_i<i-k+1 or d_queue[-1][0]>=max_element:
                max_element = d_queue[-1][0]
                current_i = d_queue[-1][1]
            if i>=k-1:
                maxes.append(max_element)
        return maxes
