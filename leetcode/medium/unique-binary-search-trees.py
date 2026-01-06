class Solution:
    def numTrees(self, n: int) -> int:
        numTrees_by_n = [1]
        for i in range(1,n):
            n_trees = 0 
            for j in range(i+1):
                if j==0:
                    left_ = 1
                else:
                    left_ = numTrees_by_n[j-1]
                if j==i:
                    right_ = 1
                else:
                    right_ = numTrees_by_n[i-j-1]
                n_trees+=left_*right_
            numTrees_by_n.append(n_trees)
        return numTrees_by_n[n-1]
