from typing import List


class Solution:
    def is_palindrom(self,string):
        if len(string)<=1:
            return True
        i = 0
        while i<len(string)//2:
            if string[i]!=string[len(string)-1-i]:
                return False
            i+=1
        return True
            
    def rec_partition(self,s,limits):
        tuple_limits = tuple([tuple(x) for x in limits])
        if tuple_limits not in self.seen_limits:
            self.seen_limits.add(tuple_limits)
            partition = []
            is_palindrom_bool = True
            for limit in limits:
                string_ = s[limit[0]:limit[1]]
                partition.append(string_)
                if not self.is_palindrom(string_):
                   is_palindrom_bool = False
                   break
            if is_palindrom_bool:
                self.all_partitions.append(partition)
        else:
            return

        for i in range(1,len(limits)):
            from_ = limits[i-1][0]
            to_ = limits[i][1]
            new_limits = limits[:i-1]+[[from_,to_]] + limits[i+1:]
            self.rec_partition(s,new_limits)

    def partition(self, s: str) -> List[List[str]]:
        self.all_partitions = []
        self.seen_limits = set()
        limits = [[i,i+1] for i in range(len(s))]
        self.rec_partition(s,limits)
        return self.all_partitions


