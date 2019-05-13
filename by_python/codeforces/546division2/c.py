n, m = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]

l1, l2 = [[] for _ in range(n+m)], [[] for _ in range(n+m)]

for i in range(n):
    for j in range(m):
        l1[i+j].append(a[i][j])
        l2[i+j].append(b[i][j])

for i in l1:
    i.sort()
for i in l2:
    i.sort()

print("YES" if l1 == l2 else "NO")