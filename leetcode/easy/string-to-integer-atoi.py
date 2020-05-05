class Solution:
    def myAtoi(self, my_str: str) -> int:
        my_str = my_str.strip()
        if my_str=="":
            return 0
        valid_characters = {str(i):i for i in range(11)}
        negative = False
        start = 0
        if my_str[0]=="-" or my_str[0] == "+":
            start =1
            if my_str[0]=="-":
                negative = True
        cleaned_str = ""
        for i in range(start,len(my_str)):
            if my_str[i] not in valid_characters:
                break
            cleaned_str+=my_str[i]
            
        final_number = 0
        for i,char in enumerate(reversed(cleaned_str)):
            if i =="0":
                return
            final_number+=valid_characters[char]*10**(i)
            if final_number>=2**31 or final_number<-2**31:
                break
                
        if negative:
            if final_number>2**31:
                return -2**31
            return -final_number
            
        if final_number>=2**31:
            return 2**31-1
        return final_number
            
            
                
            
        
