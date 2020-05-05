# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, node1: ListNode, node2: ListNode) -> ListNode: 
        first_node = ListNode(-1)
        prev = first_node
        while node1 is not None and node2 is not None:
            val1 = node1.val
            val2 = node2.val
            
            if val1 < val2:
                prev.next = node1
                prev = prev.next
                node1 = node1.next
            else:
                prev.next = node2
                prev = prev.next
                node2 = node2.next   
                
        if node1 is not None:
            prev.next = node1
        if node2 is not None:
            prev.next = node2
        return first_node.next
