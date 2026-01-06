class Solution:
    def count_tree_recurs(self,val,set_ns):
        child_trees = []
        set_ns_without = set_ns.copy()
        set_ns_without.remove(val)
        lefts = []
        rights = []
        lesser = [x for x in set_ns_without if x < val]
        greater = [x for x in set_ns_without if x > val]
        trees = []
        for element in lesser:
            lefts+=self.count_tree_recurs(element,lesser)
        for element in greater:
            rights+=self.count_tree_recurs(element,greater)
        if len(lefts) == 0:
            lefts.append(None)
        if len(rights) == 0:
            rights.append(None)
        for left_element in lefts:
            for right_element in rights:
                tree = TreeNode(val)
                tree.left = left_element
                tree.right = right_element
                trees.append(tree)
        return trees
                
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        root_trees = []
        for i in range(1,n+1):
            root_trees+=self.count_tree_recurs(i,[j+1 for j in range(n)])
        return root_trees
