def solve(day, meter):
    global n, m, cache

    if day == m: return meter >= n
    if cache[day][meter] != -1: return cache[day][meter]
    cache[day][meter] = (0.25 * solve(day+1,meter+1)) + (0.75* solve(day+1,meter+2))
    return cache[day][meter]

for _ in range(int(input())):
    n, m = map(int,input().split())
    cache = [[-1 for _ in range(2*m+1)] for _ in range(m+1)]
    res = solve(0,0)
    print("{:.10f}".format(res))