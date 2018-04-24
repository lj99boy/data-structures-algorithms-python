from stack_and_queue.queue.queue_by_list import SQueue

def mark(maze,pos):
    maze[pos[0],pos[1]] = 2

def passable(maze,pos):
    return maze[pos[0],pos[1]] == 0

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def maze_solver_queue(maze,start,end):
    if start == end:
        print("path finds")
        return

    qu = SQueue()
    mark(maze,start)
    qu.enqueue(start)
    while not qu.is_empty():
        pos = qu.dequeue()
        for i in range(4):
            nextp = (pos[0] + dirs[i][0],pos[1]+dirs[i][1])
            if passable(maze,nextp):
                if nextp == end:
                    print("path finds")
                    return

                mark(maze,nextp)
                qu.enqueue(nextp)
    print("No path")

