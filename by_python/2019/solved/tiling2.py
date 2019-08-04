#https://algospot.com/judge/problem/read/TILING2

def solve(pos):
    if pos == n: return 1
    elif pos > n : return 0
    if cache[pos] != -1: return cache[pos]
    cache[pos] = (solve(pos+1) + solve(pos+2)) % 1000000007
    return cache[pos]

for _ in range(int(input())):
    n = int(input())
    cache = [-1] * n
    print(solve(0))