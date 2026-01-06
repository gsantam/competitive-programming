class Solution:
    def longestValidParentheses(self, s: str) -> int:        
        if len(s)==0:
            return 0
        stack = [[s[0],0]]
        longest_valid = [0 for i in range(len(s))]
        max_valid = 0
        for i in range(1,len(s)):
            if s[i]==')' and len(stack)>0 and stack[-1][0]=='(':
                _,pos = stack.pop()
                longest_valid[i]+=longest_valid[pos-1] + (i-pos+1)
                max_valid = max(max_valid,longest_valid[i])
            else:
                stack.append([s[i],i])
        return max_valid
