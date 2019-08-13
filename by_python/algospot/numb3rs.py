def solve(cur, now):
    if now == 0: return 1 if cur == p else 0
    if cache[now][cur] != -1: return cache[now][cur]
    ret = 0.0
    for i in range(n):
        if board[cur][i]:
            ret += (solve(i,now-1)/connected[i])
    cache[now][cur] = ret
    return ret

for _ in range(int(input())):
    n, d, p = map(int,input().split())
    board = []
    cache = [[-1 for _ in range(n)] for _ in range(d+1)]
    connected = []
    for _ in range(n):
        board.append(list(map(int,input().split())))

    for b in board:
        connected.append(b.count(1))

    input()
    check_town = list(map(int,input().split()))
    
    res = 0.0
    for c in check_town:
        print("{:.8f}".format(solve(c, d)), end=" ")