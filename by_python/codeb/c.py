from math import inf

def find_smallest(pos, total_weight, weight_cache):
    global graph
    global cache
    global N
    global is_cycle

    if cache[pos] != -1:
        return cache[pos]
    if pos == N:
        return 0

    if pos in weight_cache and (total_weight - weight_cache[pos]) < 0:
        is_cycle = True
        return inf
    
    ret = inf

    if pos not in graph:
        return inf
    
    weight_cache[pos] = total_weight
    for n_pos, weight in graph[pos]:
        ret = min(ret,weight+find_smallest(n_pos, total_weight+weight, weight_cache))
    weight_cache.pop(pos)
    
    cache[pos]= ret
    return ret
        

graph = {}
N, M = map(int, input().split())
cache = [-1 for _ in range(N+1)]
is_cycle = False

for _ in range(M):
    s, e, w = map(int, input().split())
    if s in graph:
        graph[s].append((e,w))
    else:
        graph[s] = [(e,w)]

weight_cache = dict()

res = find_smallest(1,0, weight_cache)

if res == inf or is_cycle:
    print("bug")
else:
    print(res)