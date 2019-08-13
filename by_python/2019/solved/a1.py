#https://codeforces.com/contest/1158/problem/A

n, m = map(int, input().split())

boys = list(map(int,input().split()))
girls = list(map(int,input().split()))

boys.sort()
girls.sort()
res = 0
if boys[-1] > girls[0]:
    print(-1)
    exit(0)

for b in boys:
    res += (b*len(girls))
if boys[-1] == girls[0]:
    for g in girls:
        res += (g - boys[-1])
else:
    res += (girls[0] - boys[-2])
    for g in girls[1:]:
        res += (g - boys[-1])
print(res)