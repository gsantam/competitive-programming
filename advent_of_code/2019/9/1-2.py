numbers = [int(x) for x in open("input.txt","r").read().strip().split(",")]
length_numbers = len(numbers)

relative_base = 0
i = 0
finish = False
numbers = numbers +[0]*10000

while i<len(numbers):
    actual = numbers[i]
    str_actual = str(actual)
    code = int(str_actual[-2:])
    if actual == 99:
        break
    
    n_zeros = "".join(["0" for x in range(5-len(str_actual))])
    str_actual = n_zeros+str_actual
    mode_1 = int(str_actual[-3])
    mode_2 = int(str_actual[-4])
    mode_3 = int(str_actual[-5])
    
    if mode_1==0 and (i+1)< len(numbers):
        param_1 = numbers[i+1]
    elif mode_1==1:
        param_1 = i+1
    elif mode_1 == 2 and (i+1) < len(numbers):
        param_1 = numbers[i+1]+relative_base
        
    if mode_2 == 0 and (i+2) < len(numbers):
        param_2 = numbers[i+2]
    elif mode_2==1:
        param_2 = i+2
    elif mode_2 == 2 and (i+2) < len(numbers):
        param_2 = numbers[i+2]+relative_base
        
    if mode_3 == 0 and (i+3) < len(numbers):
        param_3 = numbers[i+3]
    elif mode_3==1:
        param_3 = i+3
    elif mode_3 == 2 and (i+3) < len(numbers):
        param_3 = numbers[i+3]+relative_base
        
    
    if code == 3:
        my_input = int(input())
        numbers[param_1] = my_input
        i+=2
        
    elif code == 4:
        #if mode_1 == 0:
        #    print(numbers[param_1])
        print(numbers[param_1])
        i+=2

    elif code == 1:
        numbers[param_3] = numbers[param_1] + numbers[param_2]
        i+=4
    elif code == 2:
        numbers[param_3] = numbers[param_1] * numbers[param_2]
        i+=4
        
    elif code == 5:
        if numbers[param_1]!=0:
            i = numbers[param_2]
        else:
            i+=3
    elif code == 6:
        if numbers[param_1]==0:
            i = numbers[param_2]
        else:
            i+=3
            
    elif code == 7:
        if numbers[param_1]<numbers[param_2]:
            numbers[param_3] = 1
        else:
            numbers[param_3] = 0
        i+=4
            
    elif code == 8:
        if numbers[param_1]==numbers[param_2]:
            numbers[param_3] = 1
        else:
            numbers[param_3] = 0
        i+=4
        
    elif code==9:
        relative_base = relative_base+numbers[param_1]
        i+=2
