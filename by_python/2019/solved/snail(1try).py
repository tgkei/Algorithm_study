#https://algospot.com/judge/problem/read/SNAIL

def solve(day_left, so_far):
    if so_far >=n: return 1
    if day_left == 0: return 0
    if cache[day_left][so_far] != -1: return cache[day_left][so_far]
    cache[day_left][so_far] = 0.75 * solve(day_left-1, so_far +2 ) + 0.25 * solve(day_left-1, so_far + 1)
    return cache[day_left][so_far]

C = int(input())
for _ in range(C):
    n, m = map(int,input().split())
    cache = [[-1 for _ in range(2*m+1)] for _ in range(m+1)]
    print("{:.8f}".format(solve(m,0)))
