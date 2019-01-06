# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
def median(historical_expenditures,d):
    
    i = 0
    number_visited = 0
    central_point = d//2 if d%2 == 0 else d//2 + 1 
    while number_visited < central_point:
        number_visited+=historical_expenditures[i]
        i+=1
    if d%2 == 1:
        return i-1
    else:
        j = i-1
        while number_visited < central_point + 1:
            number_visited+=historical_expenditures[i]
            i += 1
        return (j+i-1)/2

def activityNotifications(expenditure,d):
    n_alarms = 0
    historical_expenditures = [0 for i in range(200+1)]
    n_expenditures = 0
    trailing_array = []
    for day_expenditure in expenditure:
        trailing_array.append(day_expenditure)
        n_expenditures+=1
        if n_expenditures>d:
            if n_expenditures>d+1:
                historical_expenditures[trailing_array[len(trailing_array)-d-2]]-=1
            median_number = median(historical_expenditures,d)
            if day_expenditure >= 2*median_number:
                n_alarms+=1
        historical_expenditures[day_expenditure] +=1
    return n_alarms

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
