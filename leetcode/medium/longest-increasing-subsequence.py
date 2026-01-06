class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        best = 1
        ordered_nums = []
        for num in nums:
            if len(ordered_nums) == 0:
                ordered_nums.append([num,1])
            elif ordered_nums[len(ordered_nums)-1][0]<num:
                ordered_nums.append([num,ordered_nums[len(ordered_nums)-1][1]+1])
                best = max(best,ordered_nums[len(ordered_nums)-1][1])
            elif ordered_nums[0][0]>num:
                ordered_nums[0] = [num,ordered_nums[0][1]]
            else:
                i = 0
                j = len(ordered_nums)-1
                while (j-i)>1:
                    mid = (j+i)//2
                    if ordered_nums[mid][0]<num:
                        i = mid
                    else:
                        j = mid
                if ordered_nums[i][0]!=num and ordered_nums[j][0]!=num:
                    ordered_nums[j] = [num,ordered_nums[j][1]]
                    best = max(best,ordered_nums[j][1])
        return best
