class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        numbers = dict()
        combs = set()
        cleaned_nums = []
        for i in range(len(nums)):
            if nums[i] not in numbers:
                numbers[nums[i]] = []
            if len(numbers[nums[i]])<=2:
                numbers[nums[i]].append(i)
                cleaned_nums.append(nums[i])
                
        numbers = dict()
        for i in range(len(cleaned_nums)): 
            if cleaned_nums[i] not in numbers:
                numbers[cleaned_nums[i]] = []
            numbers[cleaned_nums[i]].append(i)
            
            
        for i in range(len(cleaned_nums)):
            for j in range(i+1,len(cleaned_nums)):
                if  - (cleaned_nums[i] + cleaned_nums[j]) in numbers:
                    for indx in numbers[-(cleaned_nums[i] + cleaned_nums[j])]:
                        if indx>j:
                            combs.add((cleaned_nums[i],cleaned_nums[j],- (cleaned_nums[i] + cleaned_nums[j])))
            
        
        return [[x[0],x[1],x[2]] for x in combs]
                        
        
