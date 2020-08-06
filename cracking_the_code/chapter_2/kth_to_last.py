class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def appendNode(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node

        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def prependNode(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def deleteWithValue(self,data):
        if self.head == None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            
            
            
def find_length(length,actual):
    if actual is None:
        return length
    else:
        actual = actual.next
        return find_length(length+1,actual)
    
"""
head -> n1 -> n2

find_length(0,head) -> find_length(1, n1) -> find_length(2,n2) -> 
find_length(3,None) -> return 3

k = 1, length = 3, lenght - k -1 = 1

actual_node = head
i = 0
actual_node = n1

"""
        
def get_k_to_end(ll,k):
    if ll.head is None:
        return "Error"

    head = ll.head
    length = find_length(0,head)
    if k > length:
        return "Error"
    
    else:
        actual_node = ll.head
        for i in range(length-k-1):
            actual_node = actual_node.next
        return actual_node
        
    
    
