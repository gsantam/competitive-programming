joints = set([int(x) for x in open("input.txt","r").readlines() if x!="\n"])
joints.add(max(joints)+3)
cum_joints = [0 for i in range(max(joints))]
cum_joints[0] = 1
cum_joints[1] = 1
for i in range(2,len(cum_joints)):
        cum_joints[i] +=  (i in joints)*(cum_joints[i-1] + cum_joints[i-2] +cum_joints[i-3])
print(max(cum_joints))
