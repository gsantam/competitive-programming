fi_2 = 1
fi_1 = 1
max_number = 0
max_numbers = []
for i in range(24000):
    fi = fi_1 + fi_2
    fi_2 = fi_1
    fi_1 = fi
    if len(str(fi)) > max_number:
        if len(str(fi)) == max_number+1:
            max_numbers.append(i+3)
        else:
            print("Error " + str(len(str(fi))-max_number))
        max_number = len(str(fi))
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(max_numbers[n-1])
