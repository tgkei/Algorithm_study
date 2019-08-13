def solve(capacity, idx): #capacity만큼 남았고 현재 idx 일 때 가능한 최대 절박함
    global cache
    if idx == n: return 0
    if cache[idx][capacity] != -1: return cache[idx][capacity]
    ret = solve(capacity, idx+1)
    if capacity>=weights[idx]:
        ret = max(ret, solve(capacity-weights[idx],idx+1)+desperate[idx])
    return ret


def recons(capacity, idx):
    global res
    if idx==n: return
    if solve(capacity,idx) == solve(capacity,idx+1): # 같다면 = 안 낀거
        recons(capacity, idx+1)
    else:
        res.append(idx)
        recons(capacity-weights[idx], idx+1)

for _ in range(int(input())):
    n, m = map(int,input().split())
    cache = [[-1 for __ in range(m+1)] for __ in range(n)]
    names = []
    weights = []
    desperate = []
    res = []
    for __ in range(n):
        name, w, d = input().split()
        w, d = int(w), int(d)
        names.append(name)
        weights.append(w)
        desperate.append(d)
    
    recons(m,0)
    need = 0
    for r in res:
        need += desperate[r]
    print(need,len(res))
    for r in res:
        print(names[r])