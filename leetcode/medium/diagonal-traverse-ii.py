class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n_diagonals = max([i+len(nums[i]) for i in range(len(nums))])
        diagonals = [[] for i in range(n_diagonals)]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i+j].append(nums[i][j])
        final = []
        for diagonal in diagonals:
            final+=list(reversed(diagonal))
        return final
