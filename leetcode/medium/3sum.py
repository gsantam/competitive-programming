    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = set()
        for i in range(len(nums)-1):
            j = i+1
            k = len(nums)-1
            while True:
                if j==k:
                    break
                sum_ = nums[i]+ nums[j]+ nums[k]
                if sum_ == 0:
                    triplets.add(tuple([nums[i], nums[j],nums[k]]))
                    j+=1
                elif sum_ > 0:
                    k-=1
                else:
                    j+=1
        return list([list(x) for x in triplets])
