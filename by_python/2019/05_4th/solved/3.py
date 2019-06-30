"""
495 div2 b
https://codeforces.com/contest/1004/problem/B
"""

n, m = map(int,input().split())

for _ in range(m): input()

for i in range(n):
    if i%2:
        print(0,end="")
    else:
        print(1,end="")