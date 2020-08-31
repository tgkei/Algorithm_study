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

    if pos in weight_cache:
        is_cycle = True
        if (total_weight - weight_cache[pos]) < 0:
            return inf, True
        return inf, False

    ret = inf

    if pos not in graph:
        return inf, False

    weight_cache[pos] = total_weight
    for n_pos, weight in graph[pos]:
        ret, is_impos = min(ret, weight+find_smallest(n_pos,
                                                      total_weight+weight, weight_cache))
        if is_impos:
            return inf, is_impos
    weight_cache.pop(pos)

    cache[pos] = ret
    return ret, False


graph = {}
N, M = map(int, input().split())
cache = [-1 for _ in range(N+1)]
is_cycle = False

for _ in range(M):
    s, e, w = map(int, input().split())
    if s in graph:
        graph[s].append((e, w))
    else:
        graph[s] = [(e, w)]

weight_cache = dict()

res, is_impos = find_smallest(1, 0, weight_cache)

if res == inf or is_impos:
    print("bug")
else:
    print(res)

