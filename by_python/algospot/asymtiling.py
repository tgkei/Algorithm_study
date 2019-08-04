def solve(cur):
    global cache
    if cur <= 1: return 1
    if cache[cur] != -1: return cache[cur]
    cache[cur] = solve(cur-1) + solve(cur-2)
    return cache[cur]

for _ in range(int(input())):
    m = int(input())
    cache = [-1] * (m+1)
    total = solve(m)
    if m%2:
        sym = solve(m//2)
    else:
        sym = solve(m//2)
        sym += solve(m//2-1)
    print((total - sym)%1000000007)