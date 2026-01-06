class Solution:
    def hammingWeight(self, n: int) -> int:
        n_total = 0
        while n!=0:
            n_total+=n%2
            n=n//2
        return n_total
