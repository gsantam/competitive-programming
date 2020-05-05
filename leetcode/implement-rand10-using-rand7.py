# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        while True:
            try_1 = rand7()
            try_2 = rand7()
            number = (try_1-1)*7 + (try_2-1)
            if number < 40:
                return number%10 + 1
        """
        :rtype: int
        """
        
