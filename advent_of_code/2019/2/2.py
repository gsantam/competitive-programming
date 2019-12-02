for a in range(100):
    for b in range(100):
        numbers = [int(x) for x in open("input.txt","r").read().strip().split(",")]
        numbers[1] = a
        numbers[2] = b
        for i in range(int(len(numbers)/4)):
            j = 4*i
            actual = numbers[j]
            if actual == 99:
                break
            if actual == 1:
                numbers[numbers[j+3]] = numbers[numbers[j+1]]+ numbers[numbers[j+2]]
            else:
                numbers[numbers[j+3]] = numbers[numbers[j+1]]*numbers[numbers[j+2]]
        if numbers[0]==19690720:
            print(100*a + b)
            break

