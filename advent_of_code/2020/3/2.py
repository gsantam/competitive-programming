maps = open("input.txt","r").read().strip().split("\n")

def get_n_trees(slope_y,slope_x):
    i = 0
    j = 0
    n_trees = 0
    while i<len(maps):
        if maps[i][j]=="#":
            n_trees+=1
        j =(j+slope_y)%len(maps[0])
        i+=slope_x
    return n_trees

print(get_n_trees(1,1)*
      get_n_trees(3,1)*
      get_n_trees(5,1)*
      get_n_trees(7,1)*
      get_n_trees(1,2))
