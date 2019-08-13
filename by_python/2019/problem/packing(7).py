#https://algospot.com/judge/problem/read/PACKING
res = []
def solve(remain, pos):
    global cache
    if pos == n: return 0
    if cache[pos][remain] != -1: return cache[pos][remain]
    ret = solve(remain, pos+1)
    if remain - weights[pos]>=0:
        ret = max(ret, priority[pos] + solve(remain-weights[pos], pos+1))
    cache[pos][remain] = ret   
    return ret

def solve2(remain, pos):    
    if pos == n: return
    if solve(remain, pos) == solve(remain, pos+1):
        solve2(remain,pos+1)
    else:
        res.append(names[pos])
        solve2(remain-weights[pos], pos+1)

c = int(input())

for _ in range(c):
    res = []
    n, w = map(int,input().split()) #물건의 수 n과 용량 w
    cache = [[-1 for _ in range(w+1)]for _ in range(n)]
    names = []
    priority = []
    weights = []
    for _ in range(n):
        name, weight, prior = input().split()
        weight = int(weight)
        prior = int(prior)
        names.append(name)
        weights.append(weight)
        priority.append(prior)
    capacity = solve(w,0)
    solve2(w,0)
    print(capacity, len(res))
    print(*res)
    