class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")":"(","}":"{","]":"["}
        stack = []
        for char in s:
            if char in close_to_open:
                if len(stack)==0 or stack.pop()!=close_to_open[char]:
                    return False
            else:
                stack.append(char)
        if len(stack)>0:
            return False
        return True
