class Solution:
    def lex_comp_bigger(self,n_1,n_2):
        i = 0   
        if int(n_1+n_2)>=int(n_2+n_1):
            return True
        return False
    
    def merge_sort(self,nums):
        if len(nums)==1:
            return nums
        left_ = self.merge_sort(nums[:len(nums)//2])
        right_ = self.merge_sort(nums[len(nums)//2:])
        i = 0
        j = 0
        result = []
        while i<len(left_) or j<len(right_):
            if i==len(left_):
                result.append(right_[j])
                j+=1
            elif j==len(right_):
                result.append(left_[i])
                i+=1
            else:
                if self.lex_comp_bigger(left_[i],right_[j]):
                    result.append(left_[i])
                    i+=1
                else:
                    result.append(right_[j])
                    j+=1
        print(result)
        return result

    def largestNumber(self, nums: List[int]) -> str:
        sorted_ = self.merge_sort([str(x) for x in nums])
        return str(int("".join(sorted_)))
