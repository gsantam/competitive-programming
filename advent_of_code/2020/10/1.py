from collections import defaultdict
joints = [int(x) for x in open("input.txt","r").readlines() if x!="\n"]
joints = sorted(joints)
dif_prevs = defaultdict(int)
dif_prevs[joints[0]]+=1
for i,joint in enumerate(joints):
    if i>0:
        dif_prevs[joint-joints[i-1]]+=1
dif_prevs[3]+=1
print(dif_prevs[1]*dif_prevs[3])
