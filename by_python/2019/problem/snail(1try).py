#https://algospot.com/judge/problem/read/SNAIL

"""def solve(day, depth):
    if day == m: return n <= depth
    if cache[depth][day] != -1: return cache[depth][day]
    cache[depth][day] = 0.75 * solve(day+1,depth+2) + 0.25 * solve(day+1,depth+1)
    return cache[depth][day]

for _ in range(int(input())):
    n, m = map(int,input().split())
    cache = [[-1 for _ in range(m)] for _ in range(2*m+1)]
    print(solve(0,0))"""