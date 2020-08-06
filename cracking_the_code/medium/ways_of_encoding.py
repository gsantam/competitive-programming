"""
data = "123"
ways_of_encodig("123")
    ways_of_encodig("23") + ways_of_encodig("3")
        1 + 1 +1
    

"""

def ways_of_encodig(message):

            
    global ways_of_encofing
    if len(message)==0:
        return 1
    if message[0]=="0":
        return 0
    if len(message)==1:
        return 1
    
    if int(message[0:2]) <= 26:
        return ways_of_encodig(message[1:])  + ways_of_encodig(message[2:])
    else:
        return ways_of_encodig(message[1:])  
    
    
print(ways_of_encodig("111111"))
        
    
        

    

    
    
