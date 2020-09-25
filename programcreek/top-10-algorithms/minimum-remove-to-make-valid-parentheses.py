class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n_open = 0
        n_close = 0
        total_close = len([char for char in s if char == ")"])
        seen_close = 0
        cleaned_s = []
        for char in s:
            if char == "(":
                if total_close - seen_close - n_open>0:
                    n_open+=1
                    cleaned_s.append("(")
            elif char == ")":
                if n_open > 0:
                    n_open-=1
                    cleaned_s.append(char)
                    n_close+=1
                seen_close+=1
            else:
                cleaned_s.append(char)
        return "".join(cleaned_s)
