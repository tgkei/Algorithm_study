"""def solve(i, num):
    global result
    if result[i][num]:
        return
    result[i][num]=1
    for temp in l[num]: # [1,2,3,4,5],[1,2,3,4]]
        for t in temp: # 1,2,3,4
            solve(i, t)

n = int(input())

l = [[] for _ in range(n)]
r = [[] for _ in range(n)]

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = list(map(int,input().split()))
    for idx, t in enumerate(temp):
        if t:
            r[i].append(idx)
            l[i].append(r[idx]) # [[[1,2,3,4],[1,2,3,4],....]....]

for idx, ll in enumerate(l): ## [[1,2,3,4],[1,2,3,4],....]
    for lll in ll: # [1,2,3,4]
        for i in lll: # 1 
            solve(idx,i)

for idx,rr in enumerate(r):
    for rrr in rr:
        result[idx][rrr]=1

for res in result:
    print(*res)"""


def solve(i,j):
    global result
    if result[i][j]:
        return
    result[i][j] = 1
    for jj in l[j]:
        solve(i,jj)

n = int(input())

l = [[] for _ in range(n)]
result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = map(int,input().split())
    for idx,t in enumerate(temp):
        if t:
            l[i].append(idx)

for i, ll in enumerate(l):
    for j in ll:
        solve(i,j)

for res in result:
    print(*res)