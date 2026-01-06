class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        final_string=[]
        counts = [a,b,c]
        letters = ['a','b','c']
        j = 0
        while True:
            target_i = -1
            for i in range(3):
                if j<=1 or (final_string[j-1]!=letters[i] or final_string[j-2]!=letters[i]):
                    if target_i==-1 or counts[i]>counts[target_i]:
                        target_i = i
            if target_i==-1 or counts[target_i]==0:
                break
            counts[target_i]-=1
            final_string.append(letters[target_i])
            j+=1
        return "".join(final_string)
