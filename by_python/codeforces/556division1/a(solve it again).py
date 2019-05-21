"""
556 division 1 a.py
https://codeforces.com/contest/1149/problem/A

from collections import Counter

n = int(input())
l = list(map(int,input().split()))

c= Counter(l)

if c[1] == 0:
    print('2 '*n)
elif c[2] == 0:
    print('1 ' * n)
else:
    print('2 1 '+"2 "*(c[2]-1) + "1 "*(c[1]-1))
"""

