# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reverseNodes(self,node,father,n,first):
        if first==True and n==self.k-1:
            self.head = node
            first = False
        if node is None:
            if n==0:
                return True, None, None
            else:
                return False, None, None
        must_reverse,join_next_group,last_this_group = self.reverseNodes(node.next,node,(n+1)%self.k,first)
        if must_reverse:
            if n!=0:
                node.next = father
            else:
                node.next = join_next_group
        if n==0 and not must_reverse:
            return True,node,None
        if n==self.k-1 and must_reverse:
            return True,join_next_group,node
        if n==0 and must_reverse:
            return True,last_this_group,last_this_group
        return must_reverse,join_next_group,last_this_group
        

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        self.k = k
        self.reverseNodes(head,None,0,True)
        return self.head
