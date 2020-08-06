class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def find_leaf_of_value(self,value,node):
        if value >=  node.info:
            child = node.right
        else:
            child = node.left
        if child is None:
            return node
        return self.find_leaf_of_value(value,child)


    def insert(self, val):
        if self.root is None:
            self.root = Node(info = val)
            self.root.level = 0
        else:
            node = Node(val)
            leaf = self.find_leaf_of_value(val,self.root)
            node.level = leaf.level + 1
            if val >= leaf.info:
                leaf.right = node
            else:
                leaf.left = node
        return self.root

        return self.root

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)

