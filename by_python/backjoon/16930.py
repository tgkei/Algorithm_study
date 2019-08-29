import sys
from collections import deque
moves = [[1,0],[-1,0],[0,1],[0,-1]]
def bfs(x,y):
    global visited
    visited[x][y] = 0
    d = deque()
    d.append((x,y))
    while d: # keep executing while queue is not empty
        cur_x,cur_y = d.popleft() 
        if cur_x == t_x and cur_y == t_y: return visited[cur_x][cur_y]
        for move in moves: # try all the possible ways to move
            for i in range(1,k+1): # try all the possible length of move
                next_x = cur_x+move[0]*i
                next_y = cur_y+move[1]*i
                if not (next_x<n and next_x>=0 and next_y<m and next_y>=0) or board[next_x][next_y] =='#': break
                if visited[next_x][next_y] != -1 and visited[next_x][next_y]==visited[cur_x][cur_y]+1: continue
                if visited[next_x][next_y] != -1: break
                visited[next_x][next_y] = visited[cur_x][cur_y] + 1 
                d.append((next_x,next_y))
    return -1 

n,m,k = map(int,sys.stdin.readline().split())
board = [input() for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]
x,y,t_x,t_y = map(lambda x :int(x) - 1,sys.stdin.readline().split())
print(bfs(x,y))