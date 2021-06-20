class Solution:
    def iterate(self,node):
        if self.k - node.val in self.values:
            self.found = True
        self.values.add(node.val)
        if node.left:
            self.iterate(node.left)
        if node.right:
            self.iterate(node.right)
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.values = set()
        self.k = k
        self.found = False
        if root:
            self.iterate(root)
        return self.found
