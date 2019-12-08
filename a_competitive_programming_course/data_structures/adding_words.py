letters_numbers = dict()
numbers_letters = dict()
while True:
    try:
        command = input()
    except Exception as e:
        break
    if command == "clear":
        letters_numbers = dict()
        numbers_letters = dict()
    elif command.startswith("def "):
        command = command[4:].split(" ")
        if int(command[1]) in letters_numbers:
            prev_letter = letters_numbers[int(command[1])]
            del numbers_letters[prev_letter]
        if command[0] in numbers_letters:
            prev_value = numbers_letters[command[0]]
            del letters_numbers[prev_value]
        
        letters_numbers[int(command[1])] = command[0]
        numbers_letters[command[0]] = int(command[1])
        
    elif command.startswith("calc "):
        clean_command = command[5:]
        command = clean_command.split(" ")
        computation = 0
        unknown = False
        prev_symbol = ""
        for i,symbol in enumerate(command[:-1]):
            if i%2==0:
                if symbol in numbers_letters:
                    if prev_symbol=="" or prev_symbol=="+":
                        computation+=numbers_letters[symbol]
                    else:
                        computation-=numbers_letters[symbol]
                else:
                    unknown = True
            prev_symbol = symbol
        if unknown is False and computation in letters_numbers:
            print(clean_command + " " + letters_numbers[computation])
        else:
            print(clean_command + " unknown")

