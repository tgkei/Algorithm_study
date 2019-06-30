"""def solve(x,y):
    if x>= n or y>=n:
        return False
    if x == n-1 and y ==n-1:
        return True
    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] = solve(x+board[x][y],y) or solve(x,y+board[x][y])
    return visited[x][y]

for _ in range(int(input())):
    n = int(input())

    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0

    if solve(0,0):
        print("YES")
    else:
        print("NO")"""

