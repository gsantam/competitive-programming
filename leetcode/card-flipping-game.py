class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        numbers = set()
        number_to_discard = set()
        for i in range(len(fronts)):
            numbers.add(fronts[i])
            numbers.add(backs[i])
            if fronts[i] == backs[i]:
                number_to_discard.add(fronts[i])
                
        numbers = sorted(numbers)
        for number in numbers:
            if number not in number_to_discard:
                return number

            
        return 0
