"""
https://www.acmicpc.net/problem/9466
"""
import sys
sys.setrecursionlimit(111111)

def solve(current):
    global visited
    global result
    global ind

    if visited[current]:
        if current in ind:
            j = ind.index(current)
            result+=j
        else:
            result+=len(ind)
        return

    visited[current] = True
    ind.append(current)
    solve(targets[current])

for _ in range(int(input())):
    n = int(input())

    targets = list(map(lambda x : int(x)-1,input().split()))

    visited= [False for _ in range(n)]
    result = 0

    for current in range(n):
        if visited[current]:
            continue
        ind=[]
        solve(current)

    print(result)