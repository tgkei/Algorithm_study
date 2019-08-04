n, m = map(int,input().split())

b = sorted(list(map(int,input().split())),reverse=True)
g = sorted(list(map(int,input().split())),reverse=True)

if g[-1] < b[0]:
    print(-1)
    exit(0)
total = sum(b) *m

g_idx = 0
b_idx = 0
while g_idx < m:
    temp = 0
    while g_idx < m and temp < m-1:
        if g[g_idx] == b[b_idx]:
            g_idx+=1
            continue
        total += (g[g_idx] - b[b_idx])
        g_idx+=1
        temp+=1
    b_idx +=1

print(total)