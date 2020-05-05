tn = telnetlib.Telnet("52.49.91.111","2003")
to_s = {"2U1L":(-1,-2),"2U1R":(1,-2),"1U2R":(2,-1),"1D2R":(2,1),"2D1R":(1,2),"2D1L":(-1,2),"1D2L":(-2,1),"1U2L":(-2,-1)}
to_s= {x:(to_s[x][1],to_s[x][0]) for x in to_s}
to_s_inv ={to_s[x]:x for x in to_s}

visited = set()
def recursive(move,tn,position):
    if move is not None:
        if (position[0] +to_s[move][0] ,position[1]+to_s[move][1]) in visited:
            return
        else:
            position = (position[0] +to_s[move][0] ,position[1]+to_s[move][1])
    else:
        position = (0,0)
    visited.add(position)

    if move is not None:
        tn.write(move.encode('ascii')+ b"\n")
    board = [[0 for i in range(5)] for j in range(5)]
    for i in range(5):
        row = tn.read_until(b"\n").decode('ascii')
        for j in range(5):
            board[i][j] = row[j]
    tn.read_until(b"\n")
    if move is not None:
        tn.read_until(b"\n")
        
    x = 2
    y = 2
    for to_ in to_s:
        pos = to_s[to_]
        if board[2+pos[0]][2+pos[1]]!="#":
            if board[2+pos[0]][2+pos[1]]=="P":
                tn.write(to_.encode('ascii')+ b"\n")
                while True:
                    print(tn.read_until(b"\n").decode('ascii'))
            recursive(to_,tn,position)
            
    if move is not None:
        move_cord = to_s[move]
        inv_move = to_s_inv[(-move_cord[0],-move_cord[1])]
        tn.write(inv_move.encode('ascii')+ b"\n")
        for i in range(5):
            row = tn.read_until(b"\n").decode('ascii')
        tn.read_until(b"\n")
        tn.read_until(b"\n")
