# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
1->2->3->4->5->NULL

1 2
1->2->3


"""

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None or n==m:
            return head
        
        from_node_prev = None
        from_node = head
        
        for i in range(m-1):
            from_node_prev = from_node
            from_node = from_node.next
         
        
        prev_node = None
        current_node = from_node
        
        for i in range(n-m+1):
            next_node =  current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            
        if m>1:
            from_node_prev.next = prev_node
            from_node.next = current_node
        else:
            head = prev_node
            from_node.next = current_node
            
        return head
            
            
        
