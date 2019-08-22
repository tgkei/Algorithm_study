"""from math import inf

def dfs(x,y,cost):
    if x == n-1 and y == m-1: return cost
    ret = inf
    for move in moves:
        next_x,next_y = x+move[0],y+move[1]
        if next_x <0 or next_y <0 or next_x>= n or next_y>=m or visited[next_x][next_y]: continue
        visited[next_x][next_y] = 1
        if int(board[next_x][next_y]): 
            ret = min(ret,dfs(next_x,next_y,cost+1))
        visited[next_x][next_y] = 0
    return ret

n, m = map(int,input().split())
moves = [[-1,0],[1,0],[0,-1],[0,1]]
visited= [[0 for _ in range(m)] for _ in range(n)]

board = [input() for _ in range(n)]
visited[0][0] = 1
print(dfs(0,0,1))"""

def bfs():
    global visited
    d = []
    d.append((0,0))
    while d:
        cur_x, cur_y = d.pop(0)
        cur_cost = visited[cur_x][cur_y]
        if cur_x == n-1 and cur_y == m-1: return cur_cost
        for move in moves:
            next_x,next_y = cur_x+move[0],cur_y+move[1]
            if next_x <0 or next_y <0 or next_x>= n or next_y>=m or visited[next_x][next_y] or not int(board[next_x][next_y]): continue
            visited[next_x][next_y] = cur_cost+1
            d.append((next_x,next_y))

n, m = map(int,input().split())
moves = [[-1,0],[1,0],[0,-1],[0,1]]
visited= [[0 for _ in range(m)] for _ in range(n)]
board = [input() for _ in range(n)]
visited[0][0] = 1
print(bfs())