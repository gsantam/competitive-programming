# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return
        
        current_node = head
        length = 1

        while current_node.next is not None:
            current_node = current_node.next
            length+=1
            
        last_node = current_node
        position_of_head = length - k%length
        
        current_node = head
        for i in range(position_of_head-1):
            current_node = current_node.next
                
        last_node.next = head
        head = current_node.next
        current_node.next = None
        return head
    
            
