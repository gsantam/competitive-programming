# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rest = 0
        prev_node = None
        while True:
            not_null = True
            actual_sum = rest
            if l1 is not None:
                actual_sum += l1.val
                l1 = l1.next
                not_null = False
            if l2 is not None:
                actual_sum+=l2.val
                l2 = l2.next
                not_null = False
            if not_null and actual_sum==0:
                break
            rest = actual_sum//10
            node = ListNode(actual_sum%10)
            if prev_node is not None:
                prev_node.next = node
            else:
                first_node = node 
            prev_node = node
            
        return first_node
