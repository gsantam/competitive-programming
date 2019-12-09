cases = int(input())
for i in range(cases):
    input()
    length = int(input())
    sequence = [int(x) for x in input().split(" ")]
    cumulated = 0
    cum_sequence = [0]
    for number in sequence:
        cumulated+=number
        cum_sequence.append(cumulated)
        
    inverse_dict = dict()
    total_cases = 0
    for number in cum_sequence:
        if number in inverse_dict:
            total_cases+=inverse_dict[number]
        if (47+number) not in inverse_dict:
            inverse_dict[(47+number)] = 0
        inverse_dict[(47+number)]+=1
    print(total_cases)

