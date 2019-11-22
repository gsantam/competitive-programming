w, p = [int(x) for x in input().split(" ")]
partitions = [int(x) for x in input().split(" ")]
partitions = [0]+ partitions + [w]
distinct_widths = [0 for x in range(w+1)]
for i in range(len(partitions)):
    for j in range(i+1,len(partitions)):
        distinct_widths[partitions[j] - partitions[i]] = 1
        
        
print(" ".join([str(i) for i in range(len(distinct_widths)) if distinct_widths[i]==1]))
    

