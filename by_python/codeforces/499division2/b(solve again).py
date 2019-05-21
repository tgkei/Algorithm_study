from collections import Counter

n, m = map(int,input().split())

l = list(map(int,input().split()))

c = Counter(l)

l = [*c.values()]
l.sort()
k=1

while sum(i//k for i in l) >=n:
    k+=1

print(k-1)