# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge2Lists(self,node1,node2):
        initial_node = ListNode(0)
        current_node = initial_node
        while node1 is not None and node2 is not None:
            if node1.val<=node2.val:
                node = ListNode(node1.val)
                node1 = node1.next
            else:
                node = ListNode(node2.val)
                node2 = node2.next
            current_node.next = node
            current_node = current_node.next
        if node1 is not None:
            current_node.next = node1
        else:
            current_node.next = node2
        
        return initial_node.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)==0:
            return
        if len(lists)==1:
            return lists[0]
        
        if len(lists)==2:
            return self.merge2Lists(lists[0],lists[1])
        
        first_half = self.mergeKLists(lists[:len(lists)//2])
        second_half = self.mergeKLists(lists[len(lists)//2:])
        
        return self.merge2Lists(first_half,second_half )   
                
                
            
        
        
