class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        if x<0:
            return False
        length_x = 0
        while True:
            if x//(10**length_x) <10:
                break
            length_x+=1
        length_x+=1
        for i in range(length_x//2 ):
            rev+=(x%10)*10**(length_x//2 - i - 1)
            x =x// 10
            
        if length_x%2==1:
            x  =x// 10
        return x==rev
