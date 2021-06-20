input_file = open("input.txt","r")
numbers = [int(i) for i in input_file.readlines()]
seen = set(numbers)
for number_1 in numbers:
    for number_2 in numbers:
        if 2020 - number_1 - number_2 in seen:
            print(number_2*number_1*(2020 - number_1 - number_2))
