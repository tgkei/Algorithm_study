#https://algospot.com/judge/problem/read/NUMB3RS

"""def prob(date,place):
    global cache
    if date == 0: return 1 if place == p else 0
    if cache[date][place] != -1 : return cache[date][place]
    ret = 0.0
    for new_place in range(n):
        if linked[place][new_place]:
                ret += (prob(date-1,new_place)/connected[new_place])
    cache[date][place] = ret
    return ret
for _ in range(int(input())):
    n, d, p = map(int,input().split())
    linked = [list(map(int,input().split())) for _ in range(n)]
    cache = [[-1 for _ in range(n)] for _ in range(101)]
    connected = [linked[i].count(1) for i in range(n)]
    t = int(input())
    target = map(int,input().split())
    for tt in target:
        print("{:0.8f}".format(prob(d,p)),end=" ")
    print()
"""

"""def bfs(date):
    global cache
    if date == d: return
    for place in range(n):
        for new in range(n):
            if cache[date][place] != 0 and linked[place][new]:
                cache[date+1][new] += cache[date][place]/connected[place]
    bfs(date+1)
    
for _ in range(int(input())):
    n, d, p = map(int,input().split())
    linked = [list(map(int,input().split())) for _ in range(n)]
    cache = [[0 for _ in range(n)] for _ in range(101)]
    cache[0][p] = 1
    connected = [linked[i].count(1) for i in range(n)]
    bfs(0)
    t = int(input())
    target = map(int,input().split())
    for tt in target:
        print("{:0.8f}".format(cache[d][tt]),end=" ")
    print()"""