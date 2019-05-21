"""pos_shape = [
              [[0,0],[0,1],[1,1]],
              [[0,0],[0,1],[-1,1]],
              [[0,0],[1,0],[1,1]],
              [[0,0],[1,0],[0,1]]
              ]

def take(which, p_or_m, y, x):
    global board

    possible = True
    for i in range(3):
        temp_x= x + pos_shape[which][i][0]
        temp_y = y + pos_shape[which][i][1]

        if temp_x <0 or temp_x >= board_x or temp_y < 0 or temp_y >= board_y:
            possible = False
        else:
            board[temp_y][temp_x] += p_or_m
            if (board[temp_y][temp_x]> 1):
                possible = False
    return possible

def cover():
    x, y = -1, -1

    for i in range(board_y):
        for j in range(board_x):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1: break
    
    if y == -1: return 1
    ret = 0
    for which in range(4):
        if take(which, 1, y, x):
            ret += cover()
        take(which,-1, y, x)
    return ret

for _ in range(int(input())):
    board_y, board_x = map(int,input().split())

    temp = [input() for _ in range(board_y)]

    board = [[0 for _ in range(board_x)] for _ in range(board_y)]

    for i in range(board_y):
        for j in range(board_x):
            if temp[i][j] == "#":
                board[i][j] = 1
            else:
                board[i][j] = 0
    
    print(cover())"""

blocks =[
    [[0,0],[1,0],[1,-1]],
    [[0,0],[1,0],[1,1]],
    [[0,0],[0,1],[1,1]],
    [[0,0],[0,1],[1,0]]
]

def possible(x,y,i,j):
    global board

    temp_x = x + blocks[i][j][0]
    temp_y = y + blocks[i][j][1]
    if temp_x < 0 or temp_x>=row or temp_y <0 or temp_y >= col:
        return False
    if board[temp_x][temp_y] == ".":
        board[temp_x][temp_y]="#"
        return True
    else:
        return False

def delete(x,y,i,j):
    global board
    temp_x = x + blocks[i][j][0]
    temp_y = y + blocks[i][j][1]
    board[temp_x][temp_y] = "."

def solve():
    global board
    x = y = -1
    for i in range(row):
        for j in range(col):
            if board[i][j] == ".":
                x = i
                y = j
                break
        if y != -1:
            break
    if x == -1:
        return 1
    
    ret = 0
    for i in range(4):
        for j in range(3):
            if not possible(x,y,i,j):
                for k in range(j-1,-1,-1):
                    delete(x,y,i,k)
                break
        else:
            ret+=solve()
            for j in range(3):
                delete(x,y,i,j)
    return ret

for _ in range(int(input())):
    row, col = map(int,input().split())
    board = []
    for _ in range(row):
        board.append(list(input()))

    print(solve())