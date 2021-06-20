class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while True:
            mid = (low+ high) //2
            guess_result = guess(mid)
            if mid == low:
                if guess(high)==0:
                    return high
            if guess_result == 0:
                return mid
            if guess_result == 1:
                low = mid
            else:
                high = mid
