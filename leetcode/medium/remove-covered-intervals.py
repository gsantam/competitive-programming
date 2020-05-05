class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted([[interval[0],-interval[1]] for interval in intervals])
        max_right = 0
        to_remove = 0
        for interval in intervals:
            from_  = interval[0]
            to_ = -interval[1]
            if to_<=max_right:
                to_remove+=1
            else:
                if from_>=max_right:
                    max_right = to_
                elif to_>max_right:
                    max_right = to_
                    
        return len(intervals) - to_remove
                

