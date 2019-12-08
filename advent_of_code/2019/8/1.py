n = 25
m = 6 
photo = open("input.txt","r").read().strip()
layers = int(len(photo)/(n*m))

layer_dict = {}
digits = set()
for layer in range(layers):
    zeros = 0
    ones = 0
    twos = 0
    for j in range(m):
        for i in range(n):
            pixel = int(photo[layer*m*n+j*n + i])
            if pixel == 1:
                ones+=1
            if pixel == 0:
                zeros+=1
            if pixel == 2:
                twos+=1   
    
    layer_dict[zeros] = ones*twos
            
min_zeros = min(layer_dict.keys())
print(layer_dict[min_zeros])
