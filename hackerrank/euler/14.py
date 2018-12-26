##### !/bin/python3

import sys

def length_number(number):
    rest = number
    seen_numbers = {}
    i = 0
    while True:
        i+=1

        if rest <MAX and catched_list[rest] !=0:
            length = catched_list[rest]
            for seen_number in seen_numbers:
                if seen_number < MAX:
                    catched_list[seen_number] = length + (len(seen_numbers) - seen_numbers[seen_number]+1)
            return catched_list[number]
            
        seen_numbers[rest] = i
        if rest %2 ==0:
            rest//=2
        else:
            rest = rest*3+1
        

t = int(input().strip())
MAX = 5*10**6+1
catched_list = [0 for x in range(MAX)]
catched_list[1] = 1
max_list = [[] for x in range(5*10**6+1)]
max_until_now = 0
max_list[0] = [0,0]

for a0 in range(t):
    n = int(input().strip())
    length_dict = dict()
    max_ = 0
    max_number = 0
    if n <= max_until_now:
        max_number = max_list[n][1]
    else:
        if n>=3732423:
            max_number = 3732423
        else:
            catched_dict = dict()
            catched_dict[1] = 1
            max_ = max_list[max_until_now][0]
            max_number = max_list[max_until_now][1]

            for number in range(max_until_now+1,n+1):
                length = length_number(number)
                if length>=max_:
                    max_ = length
                    max_number = number
                max_list[number] = [max_,max_number]
            max_until_now = n
    print(max_number)
