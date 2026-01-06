import random
class Solution:

    def __init__(self, w: List[int]):
        total_w = sum(w)
        prop_w = sorted([[w_/total_w,i] for i,w_ in enumerate(w)])
        self.cum_prop_w = [0]
        cum_sum = 0
        for i in range(len(prop_w)):
            cum_sum+=prop_w[i][0]
            self.cum_prop_w.append(cum_sum)
        self.ids = [0]+[x[1] for x in prop_w]
        print(self.cum_prop_w)
        print(self.ids)

    def pickIndex(self) -> int:
        rand = random.uniform(0, 1)
        i = 0
        j = len(self.ids)-1
        while True:
            mid = (i+j)//2
            if j-i<=1:
                return self.ids[j]
            if self.cum_prop_w[mid]<=rand:
                i = mid
            else:
                j = mid
        
