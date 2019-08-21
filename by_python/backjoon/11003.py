import sys
from collections import deque

d = deque()
n, l = map(int,sys.stdin.readline().strip().split())
nums = map(int,sys.stdin.readline().strip().split())

for i,num in enumerate(nums):
    if d and d[0][0] == i-l:
        d.popleft()
    while d and d[-1][1] >= num:
        d.pop()
    d.append([i,num])
    print(d[0][1],end= " ")