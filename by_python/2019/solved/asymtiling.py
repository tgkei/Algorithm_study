#https://algospot.com/judge/problem/read/ASYMTILING

"""def solve(pos):
    if pos == n: return 1
    elif pos > n : return 0
    if cache[pos] != -1: return cache[pos]
    cache[pos] = (solve(pos+1) + solve(pos+2)) % 1000000007
    return cache[pos]

for _ in range(int(input())):
    n = int(input())
    cache = [-1] * (n+1)
    cache[n] = 1
    total = solve(0)
    if n %2:
        m = n//2+1
        res = (total + 1000000007 - cache[m]) % 1000000007
        print(total - cache[m])
    else:
        m = cache[n//2]
        m2 = cache[n//2+1]
        res = (total + 1000000007 - m - m2) % 1000000007
        print(res)"""

def solve(remain):
    if remain == 0: return 1
    elif remain < 0: return 0
    if cache[remain] != -1: return cache[remain]
    cache[remain] = (solve(remain-1) + solve(remain-2)) % 1000000007
    return cache[remain]
for _ in range(int(input())):
    n = int(input())
    cache = [-1] * (n+1)
    total = solve(n)
    if n % 2 :
        res = (total + 1000000007 - solve(n//2)) % 1000000007
    else:
        t1= solve(n//2)
        t2 = solve(n//2-1)
        res = (total + 1000000007 - solve(n//2) - solve(n//2-1)) % 1000000007
    print(res)