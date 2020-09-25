class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        seen = dict()
        longest_sequence = 0
        for num in nums_set:
            if num not in seen:
                j=0
                find = False
                while num+j in nums_set:
                    if num+j not in seen:
                        seen[num+j] = 1
                        j+=1
                    else:
                        find = True
                        break
                        
                if not find:
                    seen[num] = j  
                else:
                    seen[num] = j + seen[num+j]
                longest_sequence = max(longest_sequence,seen[num])
        return longest_sequence
                
                    
                    
            
        
