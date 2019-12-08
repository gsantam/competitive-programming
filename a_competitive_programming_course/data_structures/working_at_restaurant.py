first = True
while True:

    n_actions = int(input())
    if n_actions == 0:
        break
    if first:
        first = False
    else:
        print("")
    pile_1 = 0
    pile_2 = 0
    for i in range(n_actions):
        action_ =input().split(" ")
        action = action_[0]
        number = int(action_[1])
        if action == "TAKE":
            if pile_1 < number:
                if pile_1>0:
                    print("TAKE 1 " + str(pile_1))
                print("MOVE 2->1 " + str(pile_2))
                print("TAKE 1 " + str(number - pile_1))
                pile_1=pile_2 + pile_1
                pile_2 = 0
            else:
                print("TAKE 1 " + str(number))
            pile_1-=number
        else:
            pile_2+=number
            print("DROP 2 "+str(number))
        
