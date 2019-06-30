"""https://codeforces.com/problemset/problem/1182/B"""

def solve(x,y):
    global is_part
    global have
    temp_x = x
    temp_y = y
    while temp_x< w and board[temp_x][temp_y+1] != "*":
        if temp_x ==w or board[temp_x][temp_y-1] == "*":
            print("NO")
            exit(0)
        is_part[temp_x][temp_y] = True
        temp_x+=1
    if temp_x == w or temp_x ==w or board[temp_x][temp_y-1] != "*":
        print("NO")
        exit(0)
    
    have = True
    right = temp_y+1
    left = temp_y -1
    while right < h and board[temp_x][right] == "*":
        is_part[temp_x][right] = True
        right+=1
    while left > -1 and board[temp_x][left] == "*":
        is_part[temp_x][left] = True
        left-=1
    while temp_x < w and board[temp_x][temp_y]=="*":
        is_part[temp_x][temp_y]= True
        temp_x+=1    

w, h = map(int,input().split())
is_part = [[False for _ in range(h)] for _ in range(w)]

have = False
board = []

for _ in range(w):
    board.append(input())

for x, b in enumerate(board):
    for y, dot in enumerate(b):
        if not have and dot == "*":
            have = True
            solve(x,y)
        elif have and not is_part[x][y] and dot == "*":
            print("NO")
            exit(0)
if not have:
    print("NO")
else:
    print("YES")