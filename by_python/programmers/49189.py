from queue import Queue


def solution(n, edge):
    answer = 0
    linked = dict()
    visited = set()

    largest = 1

    for p1, p2 in edge:
        if p1 not in linked:
            linked[p1] = [p2]
        else:
            linked[p1].append(p2)

        if p2 not in linked:
            linked[p2] = [p1]
        else:
            linked[p2].append(p1)

    q = Queue()
    visited.add(1)

    for dest in linked[1]:
        q.put((1, dest))

    while not q.empty():
        cost, dest = q.get()

        if dest in visited:
            continue

        visited.add(dest)
        for next_dest in linked[dest]:
            q.put((cost+1, next_dest))

        if cost > largest:
            largest = cost
            answer = 1
        elif cost == largest:
            answer += 1

    return answer


if __name__ == "__main__":
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, vertex))
