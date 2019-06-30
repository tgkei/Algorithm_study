"""
https://codeforces.com/contest/1066/problem/C
"""

n = int(input())
index = {}
left = 0
right = 1


for _ in range(n):
    l_or_r, idx = input().split()
    if l_or_r == "L":
        index[idx] = left
        left-=1
    elif l_or_r == "R":
        index[idx] = right
        right += 1
    else:
        print(min(index[idx]-(left+1),right-1-index[idx]))