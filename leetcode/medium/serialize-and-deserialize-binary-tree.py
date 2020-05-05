from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "[]"
        serialize_array = []
        my_queue = deque([root])
        
        while len(my_queue)>0:
            element = my_queue.pop()
            if element is None:
                serialize_array.append('null')
            else:
                serialize_array.append(element.val)
                my_queue.appendleft(element.left)
                my_queue.appendleft(element.right)
        return str(serialize_array)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        data = data[1:len(data)-1].split(", ")
        print(data)

        root = TreeNode(-1)
        my_queue = deque([(TreeNode(-1),root,"left")])
        i = -1
        while len(my_queue)>0:
            i+=1
            father,element,dir_ = my_queue.pop()
            value = data[i]
            if value != "'null'":
                element.val = int(value)
                if dir_== "left":
                    father.left = element
                else:
                    father.right = element
                left = TreeNode(-1)
                right = TreeNode(-1)
                my_queue.appendleft((element,left,"left"))
                my_queue.appendleft((element,right,"right"))
                
        return root
