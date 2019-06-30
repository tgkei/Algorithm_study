"""
https://codeforces.com/problemset/problem/1131/B
"""
n = int(input())

ans = 1
x = y = 0
for _ in range(n):
    i, j = map(int,input().split())
    if max(x,y) <= min(i,j):
        ans += (min(i,j)-max(x,y)+int(x!=y))
    x, y= i, j
print(ans)