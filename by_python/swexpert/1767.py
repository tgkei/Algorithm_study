from math import inf

def dfs(x,y, shortest, so_far,cores):
    global n
    global board
    global max_core

    if y == n:
        y = 0
        x +=1
        if x == n:
            if max_core < cores:
                max_core = cores
                return so_far
            return inf

    while board[x][y] != 1:
        y+=1
        if y == n:
            y = 0
            x +=1
            if x == n:
                if max_core <= cores:
                    max_core = cores
                    return so_far
                return so_far
    temp = 0

    possible = False

    #left
    for i in range(y):
        if board[x][i] == 1 or board[x][i] == 2:
            for j in range(i):
                board[x][j] = 0
            temp = 0
            break
        board[x][i] = 2
        temp +=1
    else:
        shortest = min(shortest,dfs(x, y+1, shortest, so_far+temp,cores+1))
        for i in range(y):
            board[x][i] = 0
        temp = 0
    #right
    for i in range(n-1, y, -1):
        if board[x][i] == 1 or board[x][i] ==2:
            for j in range(n-1,i,-1):
                board[x][j] = 0
            temp = 0
            break
        board[x][i] = 2
        temp +=1
    else:
        shortest = min(shortest,dfs(x, y+1, shortest, so_far+temp,cores+1))
        for i in range(n-1,y,-1):
            board[x][i] = 0
        temp = 0
    #up
    for i in range(x):
        if board[i][y] != 0 :
            for j in range(i):
                board[j][y] = 0
            temp = 0
            break
        board[i][y] = 2
        temp +=1
    else:
        shortest = min(shortest, dfs(x,y+1,shortest,so_far+temp,cores+1))
        for i in range(x):
            board[i][y] = 0
        temp = 0
    #bottom
    for i in range(n-1,x,-1):
        if board[i][y] != 0:
            for j in range(n-1,i,-1):
                board[j][y] = 0
            temp = 0
            break
        board[i][y] = 2
        temp += 1
    else:
        shortest = min(shortest, dfs(x,y+1,shortest,so_far+temp,cores+1))
        for i in range(n-1,x,-1):
            board[i][y] = 0
        temp = 0
    
    shortest = min(shortest, dfs(x,y+1,shortest,so_far,cores)) # fix
    return shortest

for T in range(int(input())):
    answer = -1
    max_core = 0
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    answer = dfs(0,0,inf,0,0)
    print("#{} {}".format(T+1, answer))