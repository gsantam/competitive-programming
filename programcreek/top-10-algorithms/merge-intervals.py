"""
[        ]
       [        ]
             [         ]
                  [          ]
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return intervals
        intervals = sorted(intervals)
        merged_intervals = list()
        current_left = None
        current_right = None
        for interval in intervals:
            left = interval[0]
            right = interval[1]
            if current_right is not None and left <= current_right :
                current_right = max(right,current_right)
            else:
                if current_right is not None:
                    merged_intervals.append([current_left,current_right])
                current_left = left
                current_right = right
        merged_intervals.append([current_left,current_right])
        return merged_intervals
                
        
        
