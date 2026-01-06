class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        solution = [0 for i in range(len(temperatures))]
        stack = [[temperatures[0],0]]
        for i in range(1,len(temperatures)):
            while len(stack)>0 and temperatures[i]>stack[-1][0]:
                temperature_prev,prev_i = stack.pop()
                solution[prev_i] = (i-prev_i)
            stack.append([temperatures[i],i])
        return solution
                

