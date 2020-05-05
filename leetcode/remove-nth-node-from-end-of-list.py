# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
n = 3
1->2->3


"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current_node = head
        length = 0
        while current_node is not None:
            current_node  = current_node.next
            length+=1
            
        current_node = head
        prev_node = None
        for i in range(length - n):
            prev_node = current_node
            current_node = current_node.next
        
        
        if prev_node is None:
            head = current_node.next
        else:
            prev_node.next = current_node.next
            
        return head
        
