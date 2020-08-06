def spiral(n):
    square = [[0 for i in range(n)] for i in range(n)]
    
    direction = 0
    
    j = 0
    k = 0
    
    for i in range(n**2):
        square[j][k] = i+1
        
        if direction == 0:
            if (k+1)==n or square[j][k+1]!=0:
                direction+=1
                j+=1
            else:
                k+=1
                
        if direction == 1:
            if (j+1)==n or square[j+1][k]!=0:
                direction+=1
                k-=1
            else:
                j+=1
                
        if direction == 2:
            if (k-1)==0 or square[j][k-1]!=0:
                direction+=1
                j-=1
            else:
                k-=1
                
        if direction == 3:
            if (j-1)==0 or square[j-1][k]!=0:
                direction=0
                k+=1
            else:
                j-=1
                
    return square
        
n = 5
square = spiral(5)  

for i in range(n):
    for j in range(n):
        print(square[i][j],end = " ")
    print("\n")

