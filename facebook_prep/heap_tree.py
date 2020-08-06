"""
           0
      1          2
    3 . 4 .   5 .   6
   7 8 9 10 11 12 13 14
  15

"""

class HeatTree():
    def __init__(self):
        self.array = []
        
    def add_element(self,value):
        if value is None:
            return
        self.array.append(value)
        self.swap_up(len(self.array) - 1)

        
    def remove_element_at_index(self,index):
        if index<0 or index>=len(self.array):
            return
        else:
            self.array[index] = self.array[len(self.array) - 1]
            self.array.pop()
            self.swap_down(index)
        
        
    def find_element(self,element,current_index):
        if current_index>=len(self.array):
            return None
        if self.array[current_index] == element:
            return current_index
        child_index = self.get_child_index(current_index)
        left_child_index = child_index[0]
        right_child_index = child_index[1]
        
        left_find_index = self.find_element(element,left_child_index)
        if left_find_index is None:
            right_find_index = self.find_element(element,right_child_index)
            return right_find_index
        return left_find_index
    
    def remove_element(self,element):
        element_index = self.find_element(element,0)
        self.remove_element_at_index(element_index)

        
    def get_father_index(self,index):
        return (index-1)//2
    
    def get_child_index(self,index):
        return [(index+1)*2 -1 , (index+1)*2]
    
    def swap_down(self,index):
        if index>=len(self.array):
            return
        actual_value = self.array[index]
        child_index = self.get_child_index(index)
        left_child_index = child_index[0]
        right_child_index = child_index[1]
        
        if left_child_index>=len(self.array):
            return
        
        if left_child_index<len(self.array):
            left_value = self.array[left_child_index]
        else:
            left_value = 10**10
            
        if right_child_index<len(self.array):
            right_value = self.array[right_child_index]
        else:
            right_value = 10**10
            
        tmp_value = actual_value
        if left_value < right_value:
            self.array[index] = left_value
            self.array[left_child_index] = tmp_value
            self.swap_down(left_child_index)
        else:
            self.array[index] = right_value
            self.array[right_child_index] = tmp_value
            self.swap_down(right_child_index)
            
                
    def swap_up(self,index):
        if index == 0:
            return
        father_index = self.get_father_index(index)
        father_value = self.array[father_index]
        actual_value = self.array[index]
        if actual_value > father_value:
            return
        else:
            temp_value = father_value
            self.array[father_index] = actual_value
            self.array[index] = temp_value
            self.swap_up(father_index)
            
    def print_root(self):
        print(self.array[0])
            

        


            
