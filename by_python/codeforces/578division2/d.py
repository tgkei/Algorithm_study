n, k = map(int,input().split())

board =[[1 if s == "B" else 0 for s in input()] for _ in range(n)]
white_row = []
white_column = []
temp = 0 
for row in range(n):
    for column in range(n):
        if board[row][column]:
            white_row.append(temp)
            break
    else: 
        temp +=1
        white_row.append(temp)
temp = 0
for column in range(n):
    for row in range(n):
        if board[row][column]:
            white_column.append(temp)
            break
    else: 
        temp +=1 
        white_column.append(temp)

res = -1

for r in range(n-k+1):
    for c in range(n-k+1):
        temp = 0
        temp += (white_row[-1] - white_row[r+k-1])
        temp += (white_column[-1] - white_column[c+k-1])
        if r != 0:
            temp += (white_row[r-1])
        if c != 0:
            temp += (white_column[c-1])
        
        for row in range(r,r+k):
            for column in range(n):
                if not (column>=c and column <c+k) and board[row][column]: break
            else:
                temp+=1
        for column in range(c,c+k):
            for row in range(n):
                if  not (row >= r and row<r+k) and board[row][column]: break
            else:
                temp +=1
        res = max(res,temp)
print(res)