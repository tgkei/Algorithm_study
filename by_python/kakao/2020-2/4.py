import heapq

inf = int(1e9)


def dijkstra(s, n):
    global maps

    dist = [inf for _ in range(n+1)]
    prev = dict()
    dist[s] = 0

    q = []
    heapq.heappush(q, (0, s))
    visited = set()

    while q:
        if len(visited) == n:
            break
        cur_w, cur = heapq.heappop(q)
        if cur in visited:
            continue
        visited.add(cur)

        if cur not in maps:
            continue
        for ptr, w in maps[cur]:
            if dist[ptr] > w + cur_w:
                dist[ptr] = w+cur_w
                prev[ptr] = cur
            heapq.heappush(q, (dist[ptr], ptr))

    return dist


def solution(n, s, a, b, fares):
    global maps

    answer = inf
    maps = dict()

    for fare in fares:
        p1, p2, w = fare
        if p1 not in maps:
            maps[p1] = [(p2, w)]
        else:
            maps[p1].append((p2, w))

        if p2 not in maps:
            maps[p2] = [(p1, w)]
        else:
            maps[p2].append((p1, w))

    dist = dijkstra(s, n)
    for idx, cur_weight in enumerate(dist):
        if idx == 0 or idx == s:
            continue
        if cur_weight >= answer:
            continue

        tmp_dist = dijkstra(idx, n)
        answer = min(answer, cur_weight+tmp_dist[a]+tmp_dist[b])
    return answer


if __name__ == "__main__":
    n = 6
    s = 4
    a = 6
    b = 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
        5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n, s, a, b, fares))
