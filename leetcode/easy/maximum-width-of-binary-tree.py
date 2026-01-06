class Solution:
    def traverseTree(self,node,pos,height):
        if node is None:
            return
        if len(self.leftmost_per_level)<=height:
            self.leftmost_per_level.append(pos)
        else:
            self.leftmost_per_level[height] = min(self.leftmost_per_level[height],pos)

        if len(self.rightmost_per_level)<=height:
            self.rightmost_per_level.append(pos)
        else:
            self.rightmost_per_level[height] = max(self.rightmost_per_level[height],pos)

        self.traverseTree(node.left,2*pos,height+1)
        self.traverseTree(node.right,2*pos+1,height+1)

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.leftmost_per_level = []
        self.rightmost_per_level = []
        self.traverseTree(root,0,0)
        max_width = 0
        for i in range(min(len(self.leftmost_per_level),len(self.rightmost_per_level))):
            max_width = max(max_width,self.rightmost_per_level[i]-self.leftmost_per_level[i]+1)
        return max_width
