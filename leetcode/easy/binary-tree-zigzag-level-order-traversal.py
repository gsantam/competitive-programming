from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        main_stack = [root]
        next_stack = []
        right = True
        final_list = []
        current_list = []
        while main_stack or next_stack:
            if main_stack:
                element = main_stack.pop()
                current_list.append(element.val)
                if right:
                    if element.left:
                        next_stack.append(element.left)
                    if element.right:
                        next_stack.append(element.right)
                else:
                    if element.right:
                        next_stack.append(element.right)
                    if element.left:
                        next_stack.append(element.left)
            else:
                final_list.append(current_list)
                current_list = []
                main_stack = next_stack
                next_stack = []
                right = not right
        final_list.append(current_list)
        return final_list
