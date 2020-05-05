# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        if root is not None:
            self.stack.append([root,False])
        

    def next(self) -> int:
        while True:
            current = self.stack.pop()
            node = current[0]
            count = current[1]
            if count:
                return node.val
            if node.right is not None:
                self.stack.append([node.right,False])
            self.stack.append([node,True])
            if node.left is not None:
                self.stack.append([node.left,False])            
                
        """
        @return the next smallest number
        """
        

    def hasNext(self) -> bool:
        return len(self.stack)>0
        """
        @return whether we have a next smallest number
        """
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
