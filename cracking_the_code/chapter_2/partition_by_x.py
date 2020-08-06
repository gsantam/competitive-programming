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
            
    def appendNodes(self,data_list):
        for data in data_list:
            self.appendNode(data)

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
            
    def print_list(self):
        if self.head is None:
            return
        else:
            actual_node = self.head
            while actual_node is not None:
                print(actual_node.data,end = " ")
                actual_node = actual_node.next
      
"""
x = 5
6 -> 2 -> 3 -> 2 => 6 -> 2 -> 3 -> 2 -> 6 => 2 -> 3 -> 2 -> 6


"""
            
def partition_ll_by_x(ll,x):    
    if ll.head is None:
        return
    
    last_node = ll.head
    length = 1
    while last_node.next is not None:
        last_node = last_node.next
        length+=1
        
    if length==1:
        return
            
    actual_node = ll.head
    for i in range(length):
        if actual_node.data>=x:
            node = Node(actual_node.data)
            last_node.next = node
            last_node = node
            actual_node.data = actual_node.next.data
            actual_node.next = actual_node.next.next
        else:
            actual_node = actual_node.next    
    

