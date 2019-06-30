"""
edu 59 division 2 c.py
https://codeforces.com/contest/1107/problem/C
"""

i = 0
n, k = map(int,input().split())

damages = list(map(int,input().split()))
hits = input()
dmg = 0

while i < n:
    j = i + 1
    while j < n and hits[i] == hits[j]:
        j+=1
    dmg += sum(sorted(damages[i:j],reverse= True)[:k])
    i = j
print(dmg)