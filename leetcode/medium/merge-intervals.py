"""
[        ]
       [        ]
             [         ]
                  [          ]
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:
            return
        intervals = sorted(intervals)
        final_intervals = []
        last_i = -1
        for i,interval in enumerate(intervals):
            if i == 0:
                left_most = interval[0]
                right_most = interval[1]
                continue
            if interval[0]<=right_most:
                right_most = max(right_most,interval[1])
            else:
                final_intervals.append([left_most,right_most])
                left_most = interval[0]
                right_most = interval[1]

        final_intervals.append([left_most,right_most])
            
        return final_intervals
                
        
        
