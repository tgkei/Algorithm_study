"""
https://codeforces.com/problemset/problem/1143/C
"""

n = int(input())

arr = [[0, []] for _ in range(n)]

for idx in range(n):
    par, res = map(int,input().split())
    par -=1
    if par == -2:
        arr[idx][0] = -1
        continue
    arr[par][1].append(idx)
    arr[idx][0] = res

res = []

for idx,ar in enumerate(arr):
    if ar[0] != 1 :
        continue
    for child in ar[1]:
        if not arr[child][0]:
            break
    else:
        res.append(idx+1)
if res:
    print(*sorted(res))
else:
    print("-1")