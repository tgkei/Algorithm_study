def calc_col(row,col,col_max,th,col_bound,row_bound):
    if row == row_bound:
        return -1
    minimum = board[row][col]
    maximum = board[row][col]
    pt = col+1
    cnt_col = 1

    while pt < col_bound and cnt_col <= col_max:
        maximum = max(board[row][pt],maximum)
        minimum = min(board[row][pt],minimum)
        if maximum - minimum >k:
            break
        cnt_col+=1
        pt+=1

    if cnt_col > col_max: cnt_col -=1
    result = max(calc_col(row+1,col,cnt_col,th+1,col_bound,row_bound), th * cnt_col)
    return result

for i in range(int(input())):
    row, col, k = map(int,input().split())
    board =[list(map(int,input().split())) for _ in range(row)]
    
    result = -1
    
    for r in range(row):
        for j in range(col):
            result = max(result,calc_col(r,j,col,1,col,row))

    print("Case #{}: {}".format(i+1, result))