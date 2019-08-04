#https://codeforces.com/contest/1157/problem/E
from collections import Counter
import bisect

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = Counter(b)
b = sorted(c.keys())

res = []

for aa in a:
    temp = (n - aa)%n
    idx = bisect.bisect_left(b,temp)%len(b)
    if b[idx] != temp:
        idx = bisect.bisect_right(b,temp)%len(b)
        temp = b[idx]
    while c[temp] == 0:
        idx = (idx + 1)%len(b)
        temp = b[idx]
    c[temp] -= 1
    res.append((aa+temp)%n)
print(*res)