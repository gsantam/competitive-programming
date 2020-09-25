class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combs = set()
        my_dict = dict()
        for i,num in enumerate(nums):
            if num not in my_dict:
                my_dict[num] = 0
            my_dict[num]+=1
            
        for num_1 in my_dict:
            for num_2 in my_dict:
                diff = -num_1-num_2    
                good = False
                if diff in my_dict:
                    if num_1!=num_2:
                        if diff!=num_1 and diff!=num_2:
                            good = True
                        elif my_dict[diff]>=2:
                            good =True
                    else:
                        if diff==num_1:
                            if my_dict[diff]>=3:
                                good = True
                        elif my_dict[num_1]>=2:
                            good = True
                if good:
                    combs.add(tuple(sorted([num_1,num_2,diff])))
        return combs
                            
            
