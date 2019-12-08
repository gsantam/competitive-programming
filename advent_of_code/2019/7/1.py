def run_with_config(config):
    output = 0
    for phase in config:
        n_input = 0
        numbers = [int(x) for x in open("input.txt","r").read().strip().split(",")]

        i = 0
        finish = False

        while i<len(numbers):
            actual = numbers[i]
            str_actual = str(actual)
            code = int(str_actual[-2:])
            #print(code)

            #print(code)
            if actual == 99:
                break

            n_zeros = "".join(["0" for x in range(5-len(str_actual))])
            str_actual = n_zeros+str_actual
            mode_1 = int(str_actual[-3])
            mode_2 = int(str_actual[-4])
            mode_3 = int(str_actual[-5])

            if mode_1 == 0 and (i+1) < len(numbers):
                param_1 = numbers[i+1]
            else:
                param_1 = i+1
            if mode_2 == 0 and (i+2) < len(numbers):
                param_2 = numbers[i+2]
            else:
                param_2 = i+2
            if mode_3 == 0 and (i+3) < len(numbers):
                param_3 = numbers[i+3]
            else:
                param_3 = i+3

            if code == 3:
                if n_input == 0:
                    my_input = phase
                    n_input +=1
                else:
                    my_input = output
                numbers[param_1] = my_input
                i+=2

            elif code == 4:
                if mode_1 == 0:
                    output = numbers[param_1]
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
    return output
    

max_ = 0

def backtracking(config):
    global max_
    if len(config)==5:
        final_output = run_with_config(config)
        max_ = max(final_output,max_)
    
    for i in range(0,5):
        if i not in config:
            backtracking(config + (i,))
        
backtracking(())
print(max_)
