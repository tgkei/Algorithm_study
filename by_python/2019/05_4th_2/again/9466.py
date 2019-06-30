"""
https://www.acmicpc.net/problem/9466
"""
import sys

sys.setrecursionlimit(111111)


def solve(tar):
    global visited
    global temp
    global result
    
    if visited[tar]:
        if tar in temp:
            result+=temp.index(tar)
        else:
            result+= len(temp)
        return
    visited[tar] = True
    temp.append(tar)
    solve(target[tar])

for _ in range(int(input())):
    n = int(input())
    result = 0
    target = list(map(lambda x: int(x)-1, input().split()))

    visited = [False for _ in range(n)]

    for i in range(n):
        if visited[i]:
            continue
        temp = []
        solve(i)
    print(result)