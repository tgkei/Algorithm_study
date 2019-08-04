def tiling(i):
    if i == n: return 1
    elif i > n : return 0
    if board[i] != -1: return board[i]
    res = 0
    res += tiling(i+2)
    res += tiling(i+1)
    res %= 1000000007
    board[i] = res
    return res
    

for _ in range(int(input())):
    n = int(input())
    board = [-1] * n
    res = tiling(0)
    print(res)
    