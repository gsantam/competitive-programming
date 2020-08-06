"""
hello
ello

hellp
helo
"""





def one_away(str1,str2):
    if abs(len(str1) - len(str2))>1:
        return False
    
    different = False
    if len(str1) == len(str2):
        
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if not different:
                    different = True
                else:
                    return False
    else:
        if len(str1) > len(str2):
            big = str1
            small = str2
        else:
            big = str2
            small = str1
            
        gap = 0
        for i in range(len(small)):
            if small[i] != big[i+gap]:
                if not different:
                    gap=1
                    different = True
                    if small[i]!= big[i+gap]:
                        return False
                else:
                    return False
                
    return True

                
            
            
            
