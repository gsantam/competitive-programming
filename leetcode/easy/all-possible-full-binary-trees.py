class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        trees_per_n = [[] for i in range(n+1) ]
        trees_per_n[1] = [TreeNode(0)]
        for i in range(2,n+1):
            if i%2!=0:
                for j in range(i-1):
                    for tree_left in trees_per_n[j]:
                        for tree_right in trees_per_n[i-1-j]:
                            tree = TreeNode(0)
                            tree.left = tree_left
                            tree.right = tree_right
                            trees_per_n[i].append(tree)
        return trees_per_n[n]
