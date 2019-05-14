dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [-1,0,1,-1,0,1,-1,0,1]

for _ in range(int(input())):
    board = [list(input()) for _ in range(5)]
    w_num = int(input())
    words = {input(): "NO" for _ in range(w_num)}

    for i in range(5):
        for j in range(5):
            board[i][j]