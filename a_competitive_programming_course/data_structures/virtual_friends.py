cases = int(input())
parents = dict()
children = dict()

def find(parents,friend_1):
    if parents[friend_1] == friend_1:
        return friend_1
    else:
        parents[friend_1] = find(parents,parents[friend_1])
        return parents[friend_1]

for i in range(cases):
    friendship =int(input())
    parents = dict()
    children = dict()

    for j in range(friendship):
        friends = input().split(" ")
        friend_0 = friends[0]
        friend_1 = friends[1]
        if friend_0 not in parents:
            parents[friend_0] =friend_0
            children[friend_0] = 1
        if friend_1 not in parents:
            parents[friend_1] =friend_1
            children[friend_1] = 1
            
        parent_friend_1 = find(parents,friend_1)
        parent_friend_0 = find(parents,friend_0)

        if parent_friend_0!=parent_friend_1:
            children[parent_friend_1]+=children[parent_friend_0]
        print(children[parent_friend_1])
        
        parents[parent_friend_0] = parent_friend_1
            
        
        
