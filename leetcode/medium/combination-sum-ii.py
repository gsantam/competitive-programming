class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations_idx = [[] for x in range(target+1)]
        combinations_nums = [set() for x in range(target+1)]
        for num in range(1,target+1):
            for j,candidate in enumerate(candidates):
                if num==candidate:
                    combinations_idx[num].append(set([j]))
                    combinations_nums[num].add(tuple([candidate]))
                elif num - candidate>=1:
                    for combination_idx in combinations_idx[num - candidate]:
                        if j not in combination_idx:
                            new_combination = combination_idx.copy()
                            new_combination.add(j)
                            new_combination_num = tuple(sorted([candidates[x] for x in new_combination]))
                            if new_combination_num not in combinations_nums[num]:
                                combinations_nums[num].add(new_combination_num)
                                combinations_idx[num].append(new_combination)

        return combinations_nums[target]


