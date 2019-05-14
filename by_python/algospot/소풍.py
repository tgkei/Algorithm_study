def solve(taken):
    global friends
    global n
    first = -1
    for idx,i in enumerate(taken):
        if not i:
            first = idx
            break
    if first == -1:
        return 1
    
    ret = 0
    i = first+1
    while i < n:
        if not taken[i] and friends[first][i]:
            taken[first] = taken[i] = True
            ret += solve(taken)
            taken[first] = taken[i] = False
        i+=1
    return ret

for _ in range(int(input())):
    n, m = map(int,input().split())
    
    taken = [False for _ in range(n)]
    friends = [[False for _ in range(n)] for _ in range(n)]

    nums = [*map(int,input().split())]

    for i, j in zip(nums[::2],nums[1::2]):
        friends[i][j]=friends[j][i]= True

    print(solve(taken))