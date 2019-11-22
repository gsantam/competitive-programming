import math
n = int(input())
for i in range(n):
    message = input()
    greater_power_2 = int(math.ceil(math.sqrt(len(message))))**2
    sqrt_greater_power_2 = int(math.sqrt(greater_power_2))
    
    matrix = [['' for y in range(sqrt_greater_power_2)] for x in range(sqrt_greater_power_2)]
    
    for i in range(sqrt_greater_power_2):
        for j in range(sqrt_greater_power_2):
            if i*sqrt_greater_power_2+j < len(message):
                matrix[i][j] = message[i*sqrt_greater_power_2+j]
            else:
                matrix[i][j] = '*'
    final_message = ''
    for i in range(sqrt_greater_power_2):
        for j in range(sqrt_greater_power_2): 
            if matrix[sqrt_greater_power_2-j-1][i]!='*':
                final_message+=matrix[sqrt_greater_power_2-j-1][i]
                
    print(final_message)
        
