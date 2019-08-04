"""
499 div2 b
https://codeforces.com/contest/1011/problem/B
"""

from collections import Counter

n, m = map(int,input().split())

foods = list(map(int,input().split()))
c = Counter(foods)
foods = [*c.values()]

res = 1
d = sum(foods)
while d >= n:
    d = 0
    res +=1
    for i in range(len(foods)):
        d += foods[i]//res
print(res-1)