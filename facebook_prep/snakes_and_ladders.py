from collections import deque

def quickestWayUp(ladders, snakes):
    ladders = {ladder[0]:ladder[1] for ladder in ladders}
    snakes = {snake[0]:snake[1] for snake in snakes}

    graph = {}
    for i in range(1,101):
        graph[i] = set()
        for j in range(1,7):
            current_square = i + j
            if current_square in ladders:
                graph[i].add(ladders[current_square])
            elif current_square in snakes:
                graph[i].add(snakes[current_square])
            else:
                if current_square<=100:
                    graph[i].add(current_square)

                
    visited_squares = set()
    bfs_queue = deque()
    bfs_queue.append((1,0))

    while len(bfs_queue)>0:
        current_square_ = bfs_queue.popleft()
        current_square = current_square_[0]
        distance = current_square_[1]

        if current_square not in visited_squares:
            visited_squares.add(current_square)
            if current_square==100:
                return distance
            
            for neigh_square in graph[current_square]:
                bfs_queue.append((neigh_square,distance+1))
                
    return -1
                
            
        

                
    
            

    
    
    
