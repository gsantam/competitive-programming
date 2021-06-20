input_file = open("input.txt","r")
seen = set()
for number in input_file.readlines():
    number = int(number)
    if 2020 - number in seen:
        print(number*(2020-number))
    seen.add(number)
