from math import inf

_, N = map(int, input().split())

table = dict()
cache = dict()
visited = dict()

def find_minimum(cur, tar):
    ret = inf
    if cur == tar:
        return 0
    if cur not in cache:
        return inf
    if cache[cur]:
        return cache[cur]
    if visited[cur]:
        return inf
    visited[cur] = 1

    for dest, cost in table[cur]:
        ret = min(find_minimum(dest, tar) + cost, ret)

    cache[cur] = ret

    return ret

for _ in range(N):
    source, dest, cost = input().split()
    cost = int(cost)
    if source in table:
        table[source].append((dest,cost))
    else:
        table[source] = [(dest,cost)]
        cache[source] = 0
        visited[source] = 0

N = int(input())
for _ in range(N):
    source, target = input().split()
    res = find_minimum(source,target)

    if res == inf: print(-1)
    else: print(res)

    for k in cache.keys():
        cache[k] = 0
    for k in visited.keys():
        visited[k] = 0