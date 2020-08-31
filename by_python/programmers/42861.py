from queue import PriorityQueue
from math import inf


def solution(n, costs):
    answer = 0
    linked = [[inf for _ in range(n)] for _ in range(n)]
    q = PriorityQueue()
    visited = set()

    for p1, p2, cost in costs:
        linked[p1][p2] = cost
        linked[p2][p1] = cost

    idx = 0
    visited.add(idx)
    for p2, cost in enumerate(linked[idx]):
        if cost == inf:
            continue
        q.put([cost, p2])

    while not q.empty():
        cost, idx = q.get()
        if idx in visited:
            continue

        visited.add(idx)
        answer += cost

        for p2, cost in enumerate(linked[idx]):
            if cost == inf:
                continue
            q.put([cost, p2])

    return answer


if __name__ == "__main__":
    n = 4
    costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
    print(solution(n, costs))
