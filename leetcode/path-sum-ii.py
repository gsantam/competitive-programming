# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return
        paths = []
        stack = [[root,[root.val],root.val]]
        while len(stack)>0:
            element = stack.pop()
            current_element = element[0]
            path = element[1]
            current_sum = element[2]
            if current_element.left is None and current_element.right is None:
                if current_sum == sum:
                    paths.append(path) 
                    
            else:
                if current_element.left is not None:
                    path_ = path.copy()
                    path_.append(current_element.left.val)
                    stack.append([current_element.left,path_,current_sum+current_element.left.val])
                if current_element.right is not None:
                    path_ = path.copy()
                    path_.append(current_element.right.val)
                    stack.append([current_element.right,path_,current_sum+current_element.right.val])
                        
        return paths
        
        
