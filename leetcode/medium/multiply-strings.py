class Solution:
    
    def sum_two_numbers(self,num1,num2):
        result = ""
        l1 = len(num1)
        l2 = len(num2)
        rest = 0
        for i in range(max(l1,l2)):
            if l1-1-i>=0:
                n1 = self.str_to_int[num1[l1-1-i]]
            else:
                n1 = 0
                
            if l2-1-i>=0:
                n2 = self.str_to_int[num2[l2-1-i]]
            else:
                n2 = 0   
                
            to_add = self.int_to_str[(n1+n2+rest)%10]
            rest = (n1+n2+rest)//10
            result = to_add + result
        if rest!=0:
            result = self.int_to_str[rest] + result
        return result

    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        if l1==0 or l2==0:
            return 0
        rest = 0
        self.str_to_int = {str(i):i for i in range(11)}
        self.int_to_str = {i:str(i) for i in range(11)}
        final_numbers = []
        right_zeros = ""
        for i in range(l1):
            n1 = self.str_to_int[num1[l1-1-i]]
            rest = 0
            number = ""
            for j in range(l2):
                n2 = self.str_to_int[num2[l2-1-j]]
                mult = self.int_to_str[(n1*n2 + rest)%10]
                rest = (n1*n2 + rest)//10
                number = mult + number
            if rest!=0:
                number = self.int_to_str[rest] + number
            number=number+right_zeros
            final_numbers.append(number)
            right_zeros+="0"
        final_number = final_numbers[0]
        for i in range(1,len(final_numbers)):
            final_number = self.sum_two_numbers(final_number,final_numbers[i])
        final_number = final_number.lstrip("0")
        if len(final_number)==0:
            return "0"
            
        return final_number
            
                    
            
            
            
        
