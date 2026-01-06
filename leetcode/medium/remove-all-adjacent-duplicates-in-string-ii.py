class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if len(stack)>0 and stack[-1][0]==ch:
                stack.append([ch,stack[-1][1]+1])
            else:
                stack.append([ch,1])
            if len(stack)>0 and stack[-1][1]==k:
                for i in range(k):
                    stack.pop()
        return "".join([x[0] for x in stack])
