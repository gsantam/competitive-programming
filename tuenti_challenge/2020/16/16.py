from pulp import *


lines = open("submitInput.txt","r").readlines()
i = 1
output = []
while i<len(lines):
    group_list = []
    line = lines[i].strip()
    print(line)
    floors, groups = [int(x) for x in line.split(" ")]
    for j in range(groups):
        i+=1
        line = lines[i].strip()
        employees, access_floors = [int(x) for x in line.split(" ")]
        i+=1
        floors_list = [int(x) for x in lines[i].strip().split(" ") ] 
        
        group_list.append([employees,floors_list])
        prob = LpProblem("test1", LpMinimize)
        floor_restrictions = [None for i in range(floors)]
        restrooms = LpVariable("restrooms",1,1000,cat='Integer')
        prob+=restrooms

    for k,group in enumerate(group_list):
        group_restriction= None
        for floor in group_list[k][1]:
            variable = LpVariable("g_"+str(k)+"_f_"+str(floor), 0, group_list[k][0],cat='Integer')


            if group_restriction is None:
                group_restriction = variable
            else:
                group_restriction = group_restriction+ variable

            if floor_restrictions[floor] is None:
                floor_restrictions[floor] = variable
            else:
                floor_restrictions[floor] +=variable
        prob+=group_restriction==group_list[k][0]
            #print(group)

    for floor_restriction in floor_restrictions:
        if floor_restriction is not None:
            prob+=floor_restriction<=restrooms

    result = prob.solve(GLPK(msg = 0))
    print(result)
    #print(int(prob.variables()[-1].varValue))
    output.append(int(prob.variables()[-1].varValue))
        
    i+=1
output_file = open("submitOutput.txt","w+")
output_file.write("\n".join(["Case #"+str(i+1)+": "+str(x) for i,x in enumerate(output)]))
output_file.close()
    
