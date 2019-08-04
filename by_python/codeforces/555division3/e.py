"""from bisect import bisect_left
from collections import Counter

n = int(input())
a= list(map(int,input().split()))
b= list(map(int,input().split()))
c = Counter(b)

l = sorted(c.keys())
res =[]

for temp_a in a:
    temp = n-temp_a
    idx = bisect_left(l,temp)
    if idx == len(l):
        idx = 0
    if l[idx] == temp and c[temp] > 0:
        res.append((temp_a+l[idx])%n)
        c[l[idx]] -=1
    else:
        idx1 = 0
        idx2 = idx
        while c[l[idx1]] == 0:
            idx1-=1
        while c[l[idx2]] == 0:
            idx2+=1
            idx2 %= len(l)
        if (temp_a + l[idx1])%n < (temp_a +l[idx2])%n:
            res.append((temp_a+l[idx1])%n)
            c[l[idx1]]-=1
        else:
            res.append((temp_a+l[idx2])%n)
            c[l[idx2]]-=1
print(*res)"""

n = int(input())
a = map(int, input().split())
d = [0] * n
for v in map(int, input().split()):
	d[v] += 1

r = []
for x in a:
	v = (n - x)%n
	while d[v] == 0:
		v = (v+1)%n
	r += [(x + v) % n]
	d[v] -= 1
print(*r)