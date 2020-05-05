class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A)<=2:
            return True
        cleaned_A = []
        prev = None
        for ele in A:
            if prev is None or ele!=prev:
                cleaned_A.append(ele)
            prev = ele
        for i in range(2,len(cleaned_A)):
            if not((cleaned_A[i]>=cleaned_A[i-1] and cleaned_A[i-1]>=cleaned_A[i-2]) or (cleaned_A[i]<=cleaned_A[i-1] and cleaned_A[i-1]<=cleaned_A[i-2])):
                return False

        return True
