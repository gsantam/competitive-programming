class Solution:
    def recurs(self,i):
        if i < 0 or i >= len(self.arr):
            return
        if self.seen[i] == False:
            self.can_jump[i] = True
            self.seen[i] = True
            self.recurs(i + self.arr[i])
            self.recurs(i - self.arr[i])
    def canReach(self, arr: List[int], start: int) -> bool:
        self.seen = [False for i in range(len(arr))]
        self.arr = arr
        self.can_jump = [False for i in range(len(arr))]
        self.recurs(start)
        for i in range(len(arr)):
            if arr[i]==0 and self.can_jump[i]:
                return True
        return False
