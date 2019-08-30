dp_row = [[-1 for _ in range(10)] for _ in range(11)]

dp_col = [[-1 for _ in range(11)] for _ in range(10)]

cur_x = 5
cur_y = 5

moves = input()
answer = 0
for move in moves:
    if move =="L":
        if cur_x == 0: continue
        if dp_row[cur_y][cur_x-1] == -1:
            dp_row[cur_y][cur_x-1] = 1
            res+=1
        cur_x-=1
    elif move == "R":
        if cur_x == 10: continue
        if dp_row[cur_y][cur_x] == -1:
            dp_row[cur_y][cur_x] = 1
            res+=1
        cur_x +=1
    elif move == "D":
        if cur_y == 10: continue
        if dp_col[cur_y][cur_x] == -1:
            dp_col[cur_y][cur_x] = 1
            res+=1
        cur_y +=1
    else:
        if cur_y == 0: continue
        if dp_col[cur_y-1][cur_x] == -1:
            dp_col[cur_y-1][cur_x] = 1
            res+=1
        cur_y -=1
